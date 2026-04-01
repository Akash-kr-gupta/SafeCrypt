import hashlib
import secrets
import string
import json
import os
from datetime import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


# =====================================
# PASSWORD GENERATOR
# =====================================

def generate_strong_password(length=16):
    """
    Generates a strong random password with uppercase, lowercase, digits, and symbols.
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# =====================================
# FILE HASH VERIFICATION
# =====================================

def calculate_file_hash(file_path, algorithm="sha256"):
    """
    Calculates file hash for integrity verification.
    Supports: md5, sha1, sha256, sha512
    """
    hash_obj = hashlib.new(algorithm)
    
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()


def verify_file_hash(file_path, expected_hash, algorithm="sha256"):
    """
    Verifies if file hash matches expected hash.
    """
    actual_hash = calculate_file_hash(file_path, algorithm)
    return actual_hash == expected_hash


# =====================================
# RSA KEY MANAGEMENT
# =====================================

def export_private_key_to_pem(private_key, password=None):
    """
    Exports private key to PEM format.
    Optionally encrypt with password.
    """
    if password:
        encryption_algorithm = serialization.BestAvailableEncryption(password.encode())
    else:
        encryption_algorithm = serialization.NoEncryption()
    
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )
    return pem.decode()


def export_public_key_to_pem(public_key):
    """
    Exports public key to PEM format.
    """
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode()


def load_private_key_from_pem(pem_data, password=None):
    """
    Loads private key from PEM format.
    """
    if password:
        password = password.encode()
    
    private_key = serialization.load_pem_private_key(
        pem_data.encode(),
        password=password,
        backend=default_backend()
    )
    return private_key


def load_public_key_from_pem(pem_data):
    """
    Loads public key from PEM format.
    """
    public_key = serialization.load_pem_public_key(
        pem_data.encode(),
        backend=default_backend()
    )
    return public_key


# =====================================
# RECENT FILES MANAGER
# =====================================

RECENT_FILES_PATH = "recent_files.json"


def add_to_recent(file_path, operation="encrypt"):
    """
    Adds file to recent files list.
    """
    recent_files = get_recent_files()
    
    entry = {
        "path": file_path,
        "operation": operation,
        "timestamp": datetime.now().isoformat()
    }
    
    # Remove duplicate if exists
    recent_files = [f for f in recent_files if f["path"] != file_path]
    
    # Add new entry and keep only last 10
    recent_files.insert(0, entry)
    recent_files = recent_files[:10]
    
    with open(RECENT_FILES_PATH, "w") as f:
        json.dump(recent_files, f, indent=2)


def get_recent_files():
    """
    Gets list of recent files.
    """
    if not os.path.exists(RECENT_FILES_PATH):
        return []
    
    try:
        with open(RECENT_FILES_PATH, "r") as f:
            return json.load(f)
    except:
        return []


def clear_recent_files():
    """
    Clears recent files history.
    """
    if os.path.exists(RECENT_FILES_PATH):
        os.remove(RECENT_FILES_PATH)


# =====================================
# FILE UTILITIES
# =====================================

def get_file_size_readable(file_path):
    """
    Returns human-readable file size.
    """
    size = os.path.getsize(file_path)
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    
    return f"{size:.2f} TB"


def get_file_info(file_path):
    """
    Gets file information.
    """
    return {
        "name": os.path.basename(file_path),
        "path": file_path,
        "size": get_file_size_readable(file_path),
        "size_bytes": os.path.getsize(file_path),
        "modified": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
    }
