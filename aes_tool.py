from cryptography.fernet import Fernet


# =====================================
# GENERATE RANDOM AES KEY (OPTIONAL)
# =====================================

def generate_key():
    """
    Generates a secure random Fernet key.
    """
    return Fernet.generate_key()


# =====================================
# ENCRYPT (TEXT OR BINARY)
# =====================================

def encrypt_message(data, key):
    """
    Encrypts text (str) or binary (bytes).

    - If input is string → converts to bytes
    - If input is bytes → encrypts directly
    """

    try:
        f = Fernet(key)

        if isinstance(data, str):
            data = data.encode()

        return f.encrypt(data)

    except Exception as e:
        raise Exception(f"Encryption failed: {str(e)}")


# =====================================
# DECRYPT (TEXT OR BINARY)
# =====================================

def decrypt_message(ciphertext, key):
    """
    Decrypts encrypted bytes.

    Returns:
        - str if original data was text
        - bytes if original data was binary (image, pdf, etc.)
    """

    try:
        f = Fernet(key)
        decrypted = f.decrypt(ciphertext)

        # Try to decode (text case)
        try:
            return decrypted.decode()
        except:
            return decrypted  # binary case

    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")