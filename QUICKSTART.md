# Quick Start Guide - Advanced Encryption Tool

## 🚀 Quick Setup (2 minutes)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Launch the Tool
```bash
python enhanced_gui.py
```

---

## 🎯 Common Tasks

### Task 1: Encrypt a Secret Message
1. Open enhanced_gui.py
2. Stay on "Encryption/Decryption" tab
3. Select "AES (Password-Based)"
4. Enter your message in the text box
5. Click "🔀 Generate" to create a strong password
6. Click "🔐 Encrypt"
7. Click "📋 Copy" to copy the encrypted text

### Task 2: Encrypt Multiple Files (Images, Audio, Video)
1. Go to "File Operations" tab
2. Click "➕ Add Files" and select your files:
   - 🖼️ Images (JPG, PNG, GIF, etc.)
   - 🎵 Audio files (MP3, WAV, FLAC, etc.)
   - 🎬 Videos (MP4, MKV, AVI, etc.)
   - 📄 Documents (PDF, DOCX, etc.)
   - 📦 Archives (ZIP, RAR, etc.)
3. Enter a password
4. Click "🔐 Encrypt All"
5. All files will be encrypted with .enc extension

**Bonus**: Works with ANY file type - executables, databases, etc.

### Task 3: Generate Strong Passwords
1. Go to "Tools" tab
2. Adjust length slider (8-64 characters)
3. Click "🔀 Generate"
4. Click "📋 Copy" and paste wherever needed

### Task 4: Verify File Integrity
1. Go to "Tools" tab
2. Click "📁 Select File" in File Hash Calculator
3. Copy the hash value
4. Share with others and have them verify

### Task 5: Encrypt Your Music Library
1. Go to "File Operations" tab
2. Click "➕ Add Files"
3. Select multiple audio files (MP3, WAV, FLAC, M4A, etc.)
4. Enter a strong password
5. Click "🔐 Encrypt All"
6. All songs will be encrypted securely
7. **Decrypt anytime** to restore original format

### Task 6: Protect Video Files
1. Go to "File Operations" tab
2. Click "➕ Add Files"
3. Select video files (MP4, MKV, AVI, MOV, etc.)
4. Enter a password (use "🔀 Generate" for strong password)
5. Click "🔐 Encrypt All"
6. Videos will have .enc extension
7. Keep encrypted backup in cloud safely

### Task 7: Export RSA Keys
1. Go to "Key Management" tab
2. Click "🔑 Generate Keys"
3. Click "💾 Export Keys (PEM)"
4. Select folder to save
5. Share public_key.pem with others

---

## 💡 Tips & Tricks

### Real-Time Password Strength Indicator
When you enter a password, the indicator shows:
- 🔴 **Red (Weak)**: Less than 6 characters
- 🟡 **Orange (Medium)**: 6+ characters  
- 🟢 **Green (Strong)**: 8+ chars + uppercase + numbers + symbols

**How to make it green:**
- Use 8+ characters
- Include UPPERCASE letters
- Include numbers (0-9)
- Include symbols (@#$%^&*)
- Example: `Secure@Pass123` ✅

### File Encryption - All Types Supported
- ✅ **Images**: JPG, PNG, GIF, BMP, WEBP, TIFF, SVG, ICO
- ✅ **Audio**: MP3, WAV, FLAC, M4A, AAC, OGG, WMA, OPUS
- ✅ **Video**: MP4, MKV, AVI, MOV, WMV, FLV, WEBM, 3GP
- ✅ **Documents**: PDF, DOCX, XLSX, PPTX, TXT, CSV, JSON
- ✅ **Archives**: ZIP, RAR, 7Z, TAR, GZ, ISO
- ✅ **Any other**: Executables, databases, databases, or any file type
- ✅ Batch encrypt multiple files at once
- ✅ Original files remain unchanged
- ✅ Encrypted files end with .enc

### Keyboard Shortcuts (Future)
- Ctrl+E = Encrypt
- Ctrl+D = Decrypt
- Ctrl+C = Copy output
- Ctrl+S = Save output

### File Recovery
If you forget a password:
- AES encrypted files CANNOT be recovered
- Always make backups before encryption
- Test decryption immediately after encryption

---

## 🔒 Security Reminders

⚠️ **IMPORTANT:**
- Never share your private RSA keys
- Use strong passwords (mix of letters, numbers, symbols)
- Backup encrypted files and passwords separately
- Verify file hash after transfer across networks
- Use AES for most file encryption (faster)
- Use RSA only for key exchange or signatures

---

## 📱 File Size Limits

- **AES Encryption**: Unlimited (fast, can handle GB+ files)
- **RSA Encryption**: Limited to ~190 bytes per operation (use AES for files)
- **Text Fields**: ~100,000 characters recommended
- **Batch Operations**: Process thousands of files sequentially

---

## 🎨 UI Features

### Dark Mode
- Click "🌙 Dark Mode" button (top right)
- Reduces eye strain for night use
- Automatically applied to all tabs

### Tabbed Interface
1. **Encryption/Decryption** - Basic text encryption
2. **File Operations** - Batch file processing
3. **Key Management** - RSA key operations
4. **Tools** - Password generator & file hash
5. **Recent Files** - History of operations
6. **About & Info** - Documentation

### Quick Actions
- 📋 Copy - Copy text to clipboard
- 💾 Save - Save text to file
- 🔀 Generate - Generate strong password
- 📁 Select - Choose file

---

## ❌ If Something Goes Wrong

### Error: "Invalid password or data"
→ Wrong password used for decryption  
→ File might be corrupted  

### Error: "Module not found"
→ Run: `pip install -r requirements.txt`

### Error: "No RSA key generated yet"
→ Click "Generate Keys" in Key Management tab first

### GUI won't open
→ Make sure tkinter is installed  
→ Windows: Usually pre-installed  
→ Linux: `sudo apt-get install python3-tk`

---

## 📊 Performance Tips

- ✅ Use AES for large files (much faster than RSA)
- ✅ Use batch operations for multiple files
- ✅ Encrypt files before archiving/uploading
- ✅ Use SHA256 for file hashing (good balance)
- ✅ Export keys periodically as backup

---

## 🎓 Learning Resources

Inside the tool:
- Each tab has help text
- "About & Info" tab has detailed documentation
- Hover over buttons for tooltips

---

**Version**: 2.0 (Enhanced Edition)  
**Last Updated**: April 2026  
**Status**: ✅ Ready to Use
