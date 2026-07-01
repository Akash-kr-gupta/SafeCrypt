import base64
import hashlib
import os
import sys

from flask import Flask, jsonify, request

# Ensure project root is importable when running as a Vercel function from api/index.py
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import aes_tool
import rsa_tool
import utils

app = Flask(__name__)


def _key_from_password(password: str) -> bytes:
    digest = hashlib.sha256(password.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


@app.get("/")
def root():
    return jsonify(
        {
            "name": "SafeCrypt API",
            "status": "ok",
            "endpoints": [
                "GET /health",
                "POST /aes/encrypt",
                "POST /aes/decrypt",
                "POST /rsa/generate-keys",
                "POST /rsa/encrypt",
                "POST /rsa/decrypt",
                "POST /rsa/sign",
                "POST /rsa/verify",
            ],
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.post("/aes/encrypt")
def aes_encrypt():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    password = data.get("password", "")

    if not message or not password:
        return jsonify({"error": "message and password are required"}), 400

    try:
        key = _key_from_password(password)
        encrypted = aes_tool.encrypt_message(message, key).decode("utf-8")
        return jsonify({"encrypted": encrypted})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/aes/decrypt")
def aes_decrypt():
    data = request.get_json(silent=True) or {}
    encrypted_text = data.get("encrypted", "")
    password = data.get("password", "")

    if not encrypted_text or not password:
        return jsonify({"error": "encrypted and password are required"}), 400

    try:
        key = _key_from_password(password)
        decrypted = aes_tool.decrypt_message(encrypted_text.encode("utf-8"), key)
        return jsonify({"decrypted": decrypted})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/rsa/generate-keys")
def rsa_generate_keys():
    private_key, public_key = rsa_tool.generate_keys()
    return jsonify(
        {
            "private_key_pem": utils.export_private_key_to_pem(private_key),
            "public_key_pem": utils.export_public_key_to_pem(public_key),
        }
    )


@app.post("/rsa/encrypt")
def rsa_encrypt():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    public_key_pem = data.get("public_key_pem", "")

    if not message or not public_key_pem:
        return jsonify({"error": "message and public_key_pem are required"}), 400

    try:
        public_key = utils.load_public_key_from_pem(public_key_pem)
        encrypted = rsa_tool.encrypt_message(message, public_key).hex()
        return jsonify({"encrypted_hex": encrypted})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/rsa/decrypt")
def rsa_decrypt():
    data = request.get_json(silent=True) or {}
    encrypted_hex = data.get("encrypted_hex", "")
    private_key_pem = data.get("private_key_pem", "")
    private_key_password = data.get("private_key_password")

    if not encrypted_hex or not private_key_pem:
        return jsonify({"error": "encrypted_hex and private_key_pem are required"}), 400

    try:
        private_key = utils.load_private_key_from_pem(private_key_pem, private_key_password)
        decrypted = rsa_tool.decrypt_message(bytes.fromhex(encrypted_hex), private_key)
        return jsonify({"decrypted": decrypted})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/rsa/sign")
def rsa_sign():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    private_key_pem = data.get("private_key_pem", "")
    private_key_password = data.get("private_key_password")

    if not message or not private_key_pem:
        return jsonify({"error": "message and private_key_pem are required"}), 400

    try:
        private_key = utils.load_private_key_from_pem(private_key_pem, private_key_password)
        signature = rsa_tool.sign_message(message, private_key).hex()
        return jsonify({"signature_hex": signature})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.post("/rsa/verify")
def rsa_verify():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    signature_hex = data.get("signature_hex", "")
    public_key_pem = data.get("public_key_pem", "")

    if not message or not signature_hex or not public_key_pem:
        return jsonify({"error": "message, signature_hex, and public_key_pem are required"}), 400

    try:
        public_key = utils.load_public_key_from_pem(public_key_pem)
        valid = rsa_tool.verify_signature(message, bytes.fromhex(signature_hex), public_key)
        return jsonify({"valid": bool(valid)})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
