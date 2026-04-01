import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import aes_tool
import rsa_tool
import utils
import hashlib
import base64
import re
from cryptography.fernet import Fernet
import threading
import os

# ==============================
# WINDOW SETUP
# ==============================

root = tk.Tk()
root.title("SafeCrypt")
root.geometry("1400x900")

# Theme variables
DARK_MODE = False
LIGHT_BG = "white"
LIGHT_FG = "black"
DARK_BG = "#1e1e1e"
DARK_FG = "#ffffff"

TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 12)
SMALL_FONT = ("Segoe UI", 10)
BUTTON_FONT = ("Segoe UI", 11, "bold")
TEXT_FONT = ("Consolas", 11)
CARD_BG = "#f7f7f7"

# Global variables
private_key_global = None
public_key_global = None
signature_global = None

# ==============================
# THEME MANAGEMENT
# ==============================

def toggle_theme():
    global DARK_MODE, LIGHT_BG, LIGHT_FG
    DARK_MODE = not DARK_MODE
    update_theme()

def update_theme():
    if DARK_MODE:
        bg, fg = DARK_BG, DARK_FG
        frame_bg = "#222222"
        input_bg = "#2b2b2b"
        text_bg = "#1e1e1e"
        # Keep button color same as in light mode
        button_bg = "#4CAF50"
        button_fg = "#ffffff"
        active_button_bg = "#45a049"
        border_color = "#555555"
    else:
        bg, fg = LIGHT_BG, LIGHT_FG
        frame_bg = LIGHT_BG
        input_bg = "white"
        text_bg = "white"
        button_bg = "#4CAF50"
        button_fg = "#ffffff"
        active_button_bg = "#45a049"
        border_color = "#cccccc"

    root.configure(bg=bg)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook', background=bg, borderwidth=0)
    style.configure('TNotebook.Tab', background=bg, foreground=fg, padding=[10, 5])
    style.configure('TCombobox', fieldbackground=input_bg, background=input_bg, foreground=fg, bordercolor=border_color)
    style.configure('TSeparator', background=border_color)
    style.configure('TButton', font=BUTTON_FONT, borderwidth=0, focusthickness=3, focuscolor='')

    def apply_to(widget):
        cls = widget.__class__.__name__

        try:
            if cls == 'Frame':
                widget.config(bg=frame_bg, highlightbackground=border_color, bd=0, relief=tk.FLAT)
            elif cls == 'Label':
                widget.config(bg=frame_bg, fg=fg)
            elif cls == 'Button':
                if widget is theme_btn:
                    widget.config(bg="#4CAF50", fg="white", activebackground="#3e8e41", font=BUTTON_FONT, bd=0)
                else:
                    widget.config(bg=button_bg, fg=button_fg, activebackground=active_button_bg, font=BUTTON_FONT, bd=0)
            elif cls == 'Text':
                widget.config(bg=text_bg, fg=fg, insertbackground=fg, relief=tk.SOLID, bd=1, font=TEXT_FONT)
            elif cls == 'Entry':
                widget.config(bg=input_bg, fg=fg, insertbackground=fg, highlightbackground=border_color, highlightthickness=1, font=TEXT_FONT)
            elif cls == 'Listbox':
                widget.config(bg=text_bg, fg=fg, selectbackground="#555555" if DARK_MODE else "#c0c0c0")
            elif cls == 'Scrollbar':
                widget.config(bg=frame_bg, troughcolor=frame_bg)
            elif cls == 'Spinbox':
                widget.config(bg=input_bg, fg=fg, insertbackground=fg)
        except Exception:
            pass

        for child in widget.winfo_children():
            apply_to(child)

    apply_to(root)
    theme_btn.config(text="☀️ Light Mode" if DARK_MODE else "🌙 Dark Mode")

    # Notebook is ttk and doesn't directly allow the bg option; use style instead.
    style.configure('TNotebook', background=bg)
    style.configure('TNotebook.Tab', background=bg, foreground=fg)

def apply_theme_to_widget(widget, bg_color=None, fg_color=None):
    """Deprecated: use update_theme to style all widgets."""
    pass

# ==============================
# NOTEBOOK (TABS)
# ==============================

root.configure(bg=LIGHT_BG)

# Top frame for theme button
top_frame = tk.Frame(root, bg=LIGHT_BG)
top_frame.pack(fill=tk.X, padx=10, pady=5)

theme_btn = tk.Button(top_frame, text="🌙 Dark Mode", command=toggle_theme,
                      bg="#4CAF50", fg="white", font=SMALL_FONT, bd=0, padx=10, pady=6)
theme_btn.pack(side=tk.RIGHT)

# Add a polished separator under the header
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill=tk.X, padx=15, pady=(0, 8))

# Main title
title_label = tk.Label(top_frame, text="SafeCrypt - Advanced AES & RSA Encryption Suite",
                       font=TITLE_FONT, bg=LIGHT_BG, fg=LIGHT_FG)
title_label.pack(side=tk.LEFT, padx=10)

# Notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ==============================
# TAB 1: BASIC ENCRYPTION
# ==============================

tab1 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab1, text="Encryption/Decryption")

# Encryption type
tk.Label(tab1, text="Encryption Type:", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=5)
encryption_type = tk.StringVar()
combo = ttk.Combobox(tab1, textvariable=encryption_type,
            values=["AES (Password-Based)", "RSA (Asymmetric)"],
            state="readonly", width=40)
combo.pack()
combo.config(font=TEXT_FONT)
encryption_type.set("AES (Password-Based)")

# Message
tk.Label(tab1, text="Message:", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=(15, 5))
message_entry = tk.Text(tab1, height=6, width=100, bg="white", fg="black")
message_entry.pack(padx=10)

# Password
tk.Label(tab1, text="Password (For AES):", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=(15, 5))
pass_frame = tk.Frame(tab1, bg=LIGHT_BG)
pass_frame.pack()

password_entry = tk.Entry(pass_frame, width=40, show="*", bg="white", fg="black")
password_entry.pack(side=tk.LEFT, padx=5)

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
    else:
        password_entry.config(show="")

tk.Button(pass_frame, text="👁 Show", command=toggle_password,
         bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)

tk.Button(pass_frame, text="🔀 Generate", command=lambda: gen_password_window(),
         bg="#FF9800", fg="white").pack(side=tk.LEFT, padx=5)

# Output
tk.Label(tab1, text="Result:", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=(15, 5))
output_text = tk.Text(tab1, height=6, width=100, bg="white", fg="black")
output_text.pack(padx=10)

# Buttons
btn_frame1 = tk.Frame(tab1, bg=LIGHT_BG)
btn_frame1.pack(pady=15)

def encrypt_text():
    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Enter message.")
        return
    
    output_text.delete("1.0", tk.END)
    
    try:
        if encryption_type.get() == "AES (Password-Based)":
            password = password_entry.get().strip()
            if not password:
                messagebox.showerror("Error", "Enter password.")
                return
            key = generate_key_from_password(password)
            encrypted = aes_tool.encrypt_message(message, key)
            output_text.insert(tk.END, encrypted.decode())
        else:
            global private_key_global, public_key_global
            private_key_global, public_key_global = rsa_tool.generate_keys()
            encrypted = rsa_tool.encrypt_message(message, public_key_global)
            output_text.insert(tk.END, encrypted.hex())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_text():
    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Enter encrypted message.")
        return
    
    output_text.delete("1.0", tk.END)
    
    try:
        if encryption_type.get() == "AES (Password-Based)":
            password = password_entry.get().strip()
            if not password:
                messagebox.showerror("Error", "Enter password.")
                return
            key = generate_key_from_password(password)
            decrypted = aes_tool.decrypt_message(message.encode(), key)
            output_text.insert(tk.END, decrypted)
        else:
            if not private_key_global:
                messagebox.showerror("Error", "Generate keys first by encrypting.")
                return
            decrypted = rsa_tool.decrypt_message(bytes.fromhex(message), private_key_global)
            output_text.insert(tk.END, decrypted)
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(btn_frame1, text="🔐 Encrypt", command=encrypt_text,
         bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame1, text="🔓 Decrypt", command=decrypt_text,
         bg="#2196F3", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame1, text="📋 Copy", command=lambda: copy_to_clipboard(output_text),
         bg="#FF9800", fg="white", width=15).grid(row=0, column=2, padx=5)
tk.Button(btn_frame1, text="💾 Save", command=lambda: save_output(output_text),
         bg="#009688", fg="white", width=15).grid(row=0, column=3, padx=5)

# ==============================
# TAB 2: FILE OPERATIONS
# ==============================

tab2 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab2, text="File Operations")

tk.Label(tab2, text="Batch File Encryption/Decryption", font=TITLE_FONT, 
        bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=10)

# File list
tk.Label(tab2, text="Files to Process:", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=5)
file_listbox = tk.Listbox(tab2, height=10, width=120, bg="white", fg="black")
file_listbox.pack(padx=10, pady=5)

# Scrollbar
scrollbar = tk.Scrollbar(tab2, command=file_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
file_listbox.config(yscrollcommand=scrollbar.set)

file_list = []

def add_files():
    files = filedialog.askopenfilenames()
    for file in files:
        file_list.append(file)
        file_listbox.insert(tk.END, os.path.basename(file))

def remove_selected():
    selection = file_listbox.curselection()
    if selection:
        idx = selection[0]
        file_listbox.delete(idx)
        del file_list[idx]

def clear_files():
    file_list.clear()
    file_listbox.delete(0, tk.END)

# Password for batch
tk.Label(tab2, text="Password:", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=5)
batch_password = tk.Entry(tab2, width=50, show="*", bg="white", fg="black")
batch_password.pack(padx=10)

# Batch buttons
batch_btn_frame = tk.Frame(tab2, bg=LIGHT_BG)
batch_btn_frame.pack(pady=15)

def batch_encrypt():
    if not file_list:
        messagebox.showerror("Error", "Add files first.")
        return
    
    password = batch_password.get().strip()
    if not password:
        messagebox.showerror("Error", "Enter password.")
        return
    
    key = generate_key_from_password(password)
    encrypted_count = 0
    
    for file_path in file_list:
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
            encrypted_data = aes_tool.encrypt_message(file_data, key)
            enc_path = file_path + ".enc"
            with open(enc_path, "wb") as f:
                f.write(encrypted_data)
            utils.add_to_recent(file_path, "batch_encrypt")
            encrypted_count += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt {file_path}: {str(e)}")
    
    messagebox.showinfo("Success", f"Encrypted {encrypted_count} file(s).")

def batch_decrypt():
    if not file_list:
        messagebox.showerror("Error", "Add files first.")
        return
    
    password = batch_password.get().strip()
    if not password:
        messagebox.showerror("Error", "Enter password.")
        return
    
    key = generate_key_from_password(password)
    decrypted_count = 0
    
    for file_path in file_list:
        try:
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)
            dec_path = file_path.replace(".enc", "")
            with open(dec_path, "wb") as f:
                f.write(decrypted_data)
            utils.add_to_recent(file_path, "batch_decrypt")
            decrypted_count += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt {file_path}: {str(e)}")
    
    messagebox.showinfo("Success", f"Decrypted {decrypted_count} file(s).")

tk.Button(batch_btn_frame, text="➕ Add Files", command=add_files,
         bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(batch_btn_frame, text="❌ Remove Selected", command=remove_selected,
         bg="#f44336", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(batch_btn_frame, text="🗑️ Clear All", command=clear_files,
         bg="#ff9800", fg="white", width=15).grid(row=0, column=2, padx=5)
tk.Button(batch_btn_frame, text="🔐 Encrypt All", command=batch_encrypt,
         bg="#4CAF50", fg="white", width=15).grid(row=1, column=0, padx=5, pady=10)
tk.Button(batch_btn_frame, text="🔓 Decrypt All", command=batch_decrypt,
         bg="#2196F3", fg="white", width=15).grid(row=1, column=1, padx=5, pady=10)

# ==============================
# TAB 3: KEY MANAGEMENT
# ==============================

tab3 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab3, text="Key Management")

tk.Label(tab3, text="RSA Key Management", font=TITLE_FONT, 
        bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=10)

# Key info
key_info_frame = tk.Frame(tab3, bg="white", relief=tk.SUNKEN, bd=1)
key_info_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

key_info_text = tk.Text(key_info_frame, height=15, width=140, bg="white", fg="black")
key_info_text.pack(padx=5, pady=5)

# Key buttons
key_btn_frame = tk.Frame(tab3, bg=LIGHT_BG)
key_btn_frame.pack(pady=15)

def generate_new_keys():
    global private_key_global, public_key_global
    private_key_global, public_key_global = rsa_tool.generate_keys()
    messagebox.showinfo("Success", "New RSA keys generated.")
    display_key_info()

def display_key_info():
    key_info_text.delete("1.0", tk.END)
    if private_key_global and public_key_global:
        info = f"✅ RSA Keys Generated Successfully\n\n"
        info += f"Key Size: 2048 bits\n"
        info += f"Algorithm: RSA-OAEP with SHA256\n\n"
        info += f"Private Key (PEM Format):\n"
        info += f"{'-'*60}\n"
        private_pem = utils.export_private_key_to_pem(private_key_global)
        info += private_pem[:200] + "\n... (truncated)\n\n"
        info += f"Public Key (PEM Format):\n"
        info += f"{'-'*60}\n"
        public_pem = utils.export_public_key_to_pem(public_key_global)
        info += public_pem
        key_info_text.insert(tk.END, info)
    else:
        key_info_text.insert(tk.END, "❌ No keys generated yet.\nClick 'Generate Keys' to create new RSA key pair.")

def export_keys():
    if not private_key_global or not public_key_global:
        messagebox.showerror("Error", "Generate keys first.")
        return
    
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    private_pem = utils.export_private_key_to_pem(private_key_global)
    public_pem = utils.export_public_key_to_pem(public_key_global)
    
    with open(os.path.join(folder, "private_key.pem"), "w") as f:
        f.write(private_pem)
    
    with open(os.path.join(folder, "public_key.pem"), "w") as f:
        f.write(public_pem)
    
    messagebox.showinfo("Success", "Keys exported to PEM format.")

tk.Button(key_btn_frame, text="🔑 Generate Keys", command=generate_new_keys,
         bg="#4CAF50", fg="white", width=20).pack(side=tk.LEFT, padx=5)
tk.Button(key_btn_frame, text="💾 Export Keys (PEM)", command=export_keys,
         bg="#2196F3", fg="white", width=20).pack(side=tk.LEFT, padx=5)

# ==============================
# TAB 4: TOOLS
# ==============================

tab4 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab4, text="Tools")

# Column 1: Password Generator
col1 = tk.Frame(tab4, bg=LIGHT_BG)
col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(col1, text="Password Generator", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=5)
tk.Label(col1, text="Length:", font=SMALL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack()
length_var = tk.IntVar(value=16)
tk.Spinbox(col1, from_=8, to=64, textvariable=length_var, width=10).pack()

generated_pwd = tk.Entry(col1, width=40, bg="white", fg="black")
generated_pwd.pack(pady=10)

def gen_password():
    pwd = utils.generate_strong_password(length_var.get())
    generated_pwd.delete(0, tk.END)
    generated_pwd.insert(0, pwd)

tk.Button(col1, text="🔀 Generate", command=gen_password,
         bg="#4CAF50", fg="white").pack()
tk.Button(col1, text="📋 Copy", command=lambda: copy_to_clipboard_entry(generated_pwd),
         bg="#FF9800", fg="white").pack(pady=5)

# Column 2: File Hash Calculator
col2 = tk.Frame(tab4, bg=LIGHT_BG)
col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(col2, text="File Hash Calculator", font=LABEL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=5)
tk.Label(col2, text="Algorithm:", font=SMALL_FONT, bg=LIGHT_BG, fg=LIGHT_FG).pack()
hash_algo = tk.StringVar()
ttk.Combobox(col2, textvariable=hash_algo,
            values=["SHA256", "SHA512", "MD5", "SHA1"],
            state="readonly", width=15).pack()
hash_algo.set("SHA256")

hash_result = tk.Entry(col2, width=60, bg="white", fg="black")
hash_result.pack(pady=10)

def calc_hash():
    file_path = filedialog.askopenfilename()
    if file_path:
        algo = hash_algo.get().lower()
        file_hash = utils.calculate_file_hash(file_path, algo)
        hash_result.delete(0, tk.END)
        hash_result.insert(0, file_hash)

tk.Button(col2, text="📁 Select File", command=calc_hash,
         bg="#2196F3", fg="white").pack()
tk.Button(col2, text="📋 Copy", command=lambda: copy_to_clipboard_entry(hash_result),
         bg="#FF9800", fg="white").pack(pady=5)

# ==============================
# TAB 5: RECENT FILES
# ==============================

tab5 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab5, text="Recent Files")

tk.Label(tab5, text="Recently Processed Files", font=TITLE_FONT, 
        bg=LIGHT_BG, fg=LIGHT_FG).pack(pady=10)

recent_text = tk.Text(tab5, height=20, width=140, bg="white", fg="black")
recent_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def refresh_recent():
    recent_text.delete("1.0", tk.END)
    recent_files = utils.get_recent_files()
    
    if not recent_files:
        recent_text.insert(tk.END, "No recent files yet.")
        return
    
    recent_text.insert(tk.END, "Recent Files:\n" + "-"*100 + "\n\n")
    for idx, file_info in enumerate(recent_files, 1):
        recent_text.insert(tk.END, f"{idx}. {file_info['path']}\n")
        recent_text.insert(tk.END, f"   Operation: {file_info['operation']} | Time: {file_info['timestamp']}\n\n")

recent_btn_frame = tk.Frame(tab5, bg=LIGHT_BG)
recent_btn_frame.pack(pady=10)

tk.Button(recent_btn_frame, text="🔄 Refresh", command=refresh_recent,
         bg="#2196F3", fg="white", width=15).pack(side=tk.LEFT, padx=5)
tk.Button(recent_btn_frame, text="🗑️ Clear History", command=lambda: (utils.clear_recent_files(), refresh_recent()),
         bg="#f44336", fg="white", width=15).pack(side=tk.LEFT, padx=5)

# ==============================
# TAB 6: ABOUT
# ==============================

tab6 = tk.Frame(notebook, bg=LIGHT_BG)
notebook.add(tab6, text="About & Info")

about_text = tk.Text(tab6, height=25, width=140, bg="white", fg="black")
about_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

about_content = """
╔════════════════════════════════════════════════════════════════════════════╗
║            SafeCrypt - Secure Edition          ║
╚════════════════════════════════════════════════════════════════════════════╝

📋 FEATURES:

1. TEXT ENCRYPTION
   • AES-256 (Password-Based): Symmetric encryption with password derivation
   • RSA-2048 (Asymmetric): Asymmetric encryption with OAEP padding
   • Real-time password strength indicator

2. FILE OPERATIONS
   • Single file encryption/decryption
   • Batch processing of multiple files
   • Binary-safe for all file types (images, PDFs, documents, audio, video, archives, executables)
   • Supports all media: JPG/PNG/GIF, MP3/WAV/FLAC, MP4/MKV/AVI, ZIP/RAR/7z

3. KEY MANAGEMENT
   • RSA key generation and export to PEM format
   • Support for key import from external sources
   • Secure key storage options

4. SECURITY TOOLS
   • Strong password generator (customizable length)
   • File integrity verification (SHA256, SHA512, MD5, SHA1)
   • Digital signatures (RSA-PSS with SHA256)

5. USER INTERFACE
   • Dark/Light theme toggle
   • Tabbed interface for organized workflow
   • Recent files history tracking
   • Copy-to-clipboard functionality

🔐 ENCRYPTION ALGORITHMS:

• AES (Advanced Encryption Standard)
  - Mode: Fernet (uses AES-128 in CBC mode)
  - Key Derivation: HMAC-SHA256
  - Suitable for: Text and file encryption

• RSA (Rivest–Shamir–Adleman)
  - Key Size: 2048 bits
  - Padding: OAEP with SHA256
  - Suitable for: Key exchange and digital signatures

🛡️ SECURITY BEST PRACTICES:

✓ Use strong passwords (16+ characters with mixed case, numbers, symbols)
✓ Export and backup your RSA keys securely
✓ Keep your private keys confidential
✓ Verify file hashes for integrity checking
✓ Use batch operations for processing many files

📞 DEVELOPED BY: Akash Kumar Gupta
🎓 PROJECT: Cybersecurity Internship 2026
📅 VERSION: 2.0 (Enhanced Edition)

═══════════════════════════════════════════════════════════════════════════════
"""

about_text.insert(tk.END, about_content)
about_text.config(state=tk.DISABLED)

# ==============================
# HELPER FUNCTIONS
# ==============================

def generate_key_from_password(password):
    import hashlib
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def copy_to_clipboard(text_widget):
    text = text_widget.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

def copy_to_clipboard_entry(entry_widget):
    text = entry_widget.get()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

def save_output(text_widget):
    text = text_widget.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Nothing to save.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text)
        messagebox.showinfo("Saved", f"Saved to {os.path.basename(file_path)}")

def gen_password_window():
    pwd = utils.generate_strong_password(16)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)
    messagebox.showinfo("Generated", f"Password generated: {pwd}")

# ==============================
# STARTUP
# ==============================

display_key_info()
refresh_recent()

root.mainloop()
