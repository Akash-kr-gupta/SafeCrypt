from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# =====================================
# KEY GENERATION
# =====================================

def generate_keys():
    """
    Generates a 2048-bit RSA private and public key pair.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


# =====================================
# RSA ENCRYPTION
# =====================================

def encrypt_message(message, public_key):
    """
    Encrypts a string message using RSA-OAEP.
    """

    if isinstance(message, str):
        message = message.encode()

    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


# =====================================
# RSA DECRYPTION
# =====================================

def decrypt_message(ciphertext, private_key):
    """
    Decrypts RSA encrypted bytes.
    Returns string if possible.
    """

    decrypted = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    try:
        return decrypted.decode()
    except:
        return decrypted


# =====================================
# DIGITAL SIGNATURE (PSS + SHA256)
# =====================================

def sign_message(message, private_key):
    """
    Signs a message using RSA-PSS.
    """

    if isinstance(message, str):
        message = message.encode()

    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )


# =====================================
# VERIFY DIGITAL SIGNATURE
# =====================================

def verify_signature(message, signature, public_key):
    """
    Verifies RSA-PSS signature.
    Returns True if valid, False otherwise.
    """

    if isinstance(message, str):
        message = message.encode()

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False