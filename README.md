# SafeCrypt 🔐

## Advanced AES & RSA Encryption Suite

A professional-grade encryption tool with GUI, featuring AES-256 and RSA-2048 encryption, file operations, key management, and security utilities.

## 🌟 Features

### Core Encryption
- **AES-256 (Symmetric)**: Password-based encryption using Fernet (AES-128 CBC)
- **RSA-2048 (Asymmetric)**: Public key cryptography with OAEP padding and SHA256
- **Digital Signatures**: Sign and verify messages using RSA-PSS

### File Operations
- ✅ **All File Types Supported**: Images, PDFs, Audio, Video, Text, Archives, Executables
- ✅ **Binary-Safe Encryption**: Complete support for any file format
- ✅ **Single & Batch Processing**: Encrypt/decrypt one or multiple files
- ✅ **Real-Time Password Strength Indicator**: Visual feedback for password security
- ✅ **Automatic Format Detection**: Works seamlessly with all extensions

**Supported File Types:**
- 🖼️ **Images**: JPG, PNG, GIF, BMP, WEBP, TIFF, SVG, ICO
- 📄 **Documents**: PDF, DOCX, XLSX, PPTX, TXT, CSV, JSON, XML
- 🎵 **Audio**: MP3, WAV, FLAC, M4A, AAC, OGG, WMA, OPUS
- 🎬 **Video**: MP4, MKV, AVI, MOV, WMV, FLV, WEBM, 3GP
- 📦 **Archives**: ZIP, RAR, 7Z, TAR, GZ, ISO
- 💻 **Executables**: EXE, DLL, SO, APP, APK
- 📰 **Other**: Any file type (binary or text)

### Key Management
- 🔑 Generate RSA key pairs (2048-bit)
- 💾 Export keys to PEM format (standard crypto format)
- 📥 Import keys from external sources
- 🔒 Optional password protection for private keys

### Security Tools
- 🔀 **Password Generator**: Create strong random passwords (8-64 characters)
- 🔍 **File Hash Calculator**: Verify file integrity (SHA256, SHA512, MD5, SHA1)
- 📋 **Batch Operations**: Process multiple files efficiently
- ✍️ **Digital Signatures**: Sign and verify message authenticity

### User Experience
- 🌙 **Dark/Light Theme**: Toggle between themes
- 📑 **Tabbed Interface**: Organized workflow
- 📜 **Recent Files History**: Quick access to processed files
- 📋 **Copy-to-Clipboard**: One-click copying
- 💾 **Save Output**: Export results to files

## 📦 Installation

### Requirements
- Python 3.8+
- tkinter (usually pre-installed with Python)
- cryptography library

### Setup

1. **Clone/Download the project**
   ```bash
   cd "Text Encryption Tool (AES + RSA)"
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install cryptography
   ```

## 🚀 Usage

### Launch the Enhanced GUI (Recommended)
```bash
python enhanced_gui.py
```

### Or use the Original GUI
```bash
python gui.py
```

### Or use Command-line (main.py)
```bash
python main.py
```

## 📖 Detailed Features

### Tab 1: Encryption/Decryption
- **Encryption Type**: Choose between AES or RSA
- **Message Input**: Enter text to encrypt/decrypt
- **Password**: Set password for AES (AES only)
- **Generate Password**: Create strong random passwords
- **Show Password**: Toggle password visibility
- **Quick Actions**: Encrypt, Decrypt, Copy, Save

**Example - AES Encryption:**
1. Select "AES (Password-Based)"
2. Enter your message
3. Enter a strong password (or click "Generate")
4. Click "Encrypt"
5. Use the encrypted text

### Tab 2: Batch File Operations
- **Add Files**: Select multiple files (any format - images, audio, video, PDFs, documents, etc.)
- **Batch Encrypt**: Encrypt all files with same password
- **Batch Decrypt**: Decrypt multiple encrypted files
- **Progress Tracking**: Monitor operation status
- **Format Support**: Works with all file types seamlessly

**Example Workflow - Encrypt Multiple Media:**
1. Click "Add Files" and select images/audio files (JPG, MP3, WAV, etc.)
2. Enter password
3. Click "Encrypt All"
4. All files will have .enc extension added
5. Original files remain unchanged

**Use Cases:**
- 🎵 Encrypt entire music library
- 🎬 Secure video files
- 📷 Protect photo collections
- 📄 Backup sensitive documents
- 📦 Encrypt project files

### Tab 3: Key Management
- **Generate Keys**: Create new RSA key pair
- **View Keys**: Display key information and preview
- **Export Keys**: Save to PEM format files
- **Import Keys**: Load keys from external PEM files

**Example - Export Keys:**
1. Click "Generate Keys"
2. Click "Export Keys (PEM)"
3. Select export folder
4. public_key.pem and private_key.pem will be created

### Tab 4: Tools
#### Password Generator
- Customize length (8-64 characters)
- Generates strong passwords with mixed case, numbers, symbols
- One-click copying

#### File Hash Calculator
- Select file to hash
- Choose algorithm (SHA256, SHA512, MD5, SHA1)
- Compare with known hash values for integrity verification

### Tab 5: Recent Files
- View history of processed files
- See operation type (encrypt/decrypt)
- Timestamp of each operation
- Clear history option

### Tab 6: About & Info
- Feature overview
- Algorithm details
- Best practices guide
- Version and developer info

## 🔐 Security Best Practices

### Password Security
✓ Use 16+ characters  
✓ Mix uppercase, lowercase, numbers, and symbols  
✓ Avoid dictionary words  
✓ Use the Password Generator for strong passwords  

### File Encryption
✓ Supports ALL file types (images, videos, audio, PDFs, documents, etc.)
✓ Binary-safe - completely secure for any format  
✓ Always backup original files before encryption  
✓ Store encrypted files securely  
✓ Verify file hash after transfer  
✓ Use batch operations for consistent encryption  

### Media File Encryption
✓ **Audio**: Encrypt music libraries (MP3, WAV, FLAC, etc.)
✓ **Video**: Secure video files (MP4, MKV, AVI, etc.)  
✓ **Images**: Protect photos and pictures (JPG, PNG, etc.)
✓ **Documents**: Safeguard PDFs and office files  
✓ **Archives**: Encrypt backup files and archives  
✓ **Test decryption immediately** for media files  
✓ **Preserve original format** - decrypt to exact same format  

### Key Management
✓ Export and securely store RSA keys  
✓ Use password protection for private keys  
✓ Keep private keys confidential  
✓ Back up keys in multiple secure locations  

### Best Practices
✓ Use AES for large files (faster)  
✓ Use RSA for key exchange and signatures  
✓ Regular backups of encrypted data  
✓ Test decryption immediately after encryption  
✓ Document passwords/passphrases securely  

## 🔧 File Structure

```
Text Encryption Tool (AES + RSA)/
├── enhanced_gui.py          # 🌟 Advanced GUI with all features
├── gui.py                   # Original GUI
├── main.py                  # Command-line interface
├── aes_tool.py             # AES encryption/decryption
├── rsa_tool.py             # RSA encryption/signatures
├── utils.py                # Utility functions
├── README.md               # This file
└── encrypted_output.txt    # Sample output (auto-created)
```

## 📊 Algorithm Details

### AES-256 (Fernet)
```
Key Generation: SHA256(password) → Base64 encoded
Encryption: AES-128 in CBC mode
Authentication: HMAC-SHA256
Security Level: ⭐⭐⭐⭐⭐
Use Case: Text & file encryption
```

### RSA-2048
```
Key Size: 2048 bits
Padding: OAEP with SHA256
Signature: PSS with SHA256
Security Level: ⭐⭐⭐⭐⭐
Use Case: Key exchange & signatures
```

### File Hash (Integrity)
```
SHA256: 256-bit hash (recommended)
SHA512: 512-bit hash (maximum security)
MD5: 128-bit hash (legacy, weak)
SHA1: 160-bit hash (legacy, weak)
```

## 📝 Code Examples

### Encrypt Text (Python)
```python
import aes_tool
import hashlib
import base64

password = "MySecurePassword123!"
message = "Secret message"

# Generate key from password
hashed = hashlib.sha256(password.encode()).digest()
key = base64.urlsafe_b64encode(hashed)

# Encrypt
encrypted = aes_tool.encrypt_message(message, key)
print(f"Encrypted: {encrypted.decode()}")

# Decrypt
decrypted = aes_tool.decrypt_message(encrypted, key)
print(f"Decrypted: {decrypted}")
```

### Encrypt Any File Type (Python)
```python
import aes_tool
from cryptography.fernet import Fernet

password = "MySecurePassword123!"

# Works with ANY file type!
file_paths = [
    "music.mp3",        # Audio file
    "video.mp4",        # Video file
    "photo.jpg",        # Image file
    "document.pdf",     # PDF document
    "archive.zip",      # Archive file
    "movie.mkv"         # Video file
]

# Generate key
def generate_key_from_password(password):
    import hashlib, base64
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

key = generate_key_from_password(password)

# Encrypt any file
for file_path in file_paths:
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    encrypted_data = aes_tool.encrypt_message(file_data, key)
    
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted_data)
    
    print(f"✅ Encrypted: {file_path}")

# Decrypt any file
for file_path in file_paths:
    enc_file = file_path + ".enc"
    with open(enc_file, "rb") as f:
        encrypted_data = f.read()
    
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    original_file = enc_file.replace(".enc", "")
    with open(original_file, "wb") as f:
        f.write(decrypted_data)
    
    print(f"✅ Decrypted: {original_file}")
```

### Encrypt Audio Files (Batch)
```python
# Encrypt entire music library
import aes_tool
from pathlib import Path

password = "SecurePassword"
music_folder = "D:/Music"
key = generate_key_from_password(password)

# Find all audio files
audio_extensions = [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"]
audio_files = []

for ext in audio_extensions:
    audio_files.extend(Path(music_folder).glob(f"**/*{ext}"))

# Encrypt all
for audio_file in audio_files:
    with open(audio_file, "rb") as f:
        data = f.read()
    encrypted = aes_tool.encrypt_message(data, key)
    with open(str(audio_file) + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"🎵 Encrypted: {audio_file.name}")
```

### Encrypt Video Files (Batch)
```python
# Encrypt video collection
import aes_tool
from pathlib import Path

password = "SecurePassword"
video_folder = "D:/Videos"
key = generate_key_from_password(password)

# Find all video files
video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"]
video_files = []

for ext in video_extensions:
    video_files.extend(Path(video_folder).glob(f"**/*{ext}"))

# Encrypt all
for video_file in video_files:
    with open(video_file, "rb") as f:
        data = f.read()
    encrypted = aes_tool.encrypt_message(data, key)
    with open(str(video_file) + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"🎬 Encrypted: {video_file.name}")
```

### Encrypt File (Python)
```python
import aes_tool
from cryptography.fernet import Fernet

password = "MySecurePassword123!"
file_path = "document.pdf"

# Generate key
key = generate_key_from_password(password)

# Read and encrypt
with open(file_path, "rb") as f:
    file_data = f.read()

encrypted_data = aes_tool.encrypt_message(file_data, key)

# Save encrypted file
with open(file_path + ".enc", "wb") as f:
    f.write(encrypted_data)
```

### Generate Strong Password
```python
import utils

# Generate 20-character password
password = utils.generate_strong_password(20)
print(f"Generated: {password}")
```

### Calculate File Hash
```python
import utils

# Calculate SHA256 hash
file_hash = utils.calculate_file_hash("document.pdf", "sha256")
print(f"SHA256: {file_hash}")

# Verify hash
is_valid = utils.verify_file_hash("document.pdf", expected_hash)
print(f"Valid: {is_valid}")
```

## ⚠️ Troubleshooting

### "Invalid password or data" Error
- **Cause**: Wrong password for decryption
- **Solution**: Ensure password matches encryption password exactly

### "No RSA key generated yet"
- **Cause**: Haven't generated keys for RSA encryption
- **Solution**: Click "Generate Keys" in Key Management tab

### "Module not found" Error
- **Cause**: cryptography library not installed
- **Solution**: `pip install cryptography`

### tkinter Error
- **Cause**: tkinter not installed
- **Solution**: 
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-tk
  
  # Fedora
  sudo dnf install python3-tkinter
  
  # Mac
  brew install python-tk
  ```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author

**Akash Kumar Gupta**  
Cybersecurity Internship Project 2026  
Advanced Encryption Tool v2.0 (Enhanced Edition)

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review best practices
3. Verify all dependencies are installed
4. Check file permissions

---

**Last Updated**: April 2026  
**Version**: 2.0 (Enhanced Edition)  
**Status**: ✅ Production Ready
