import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import aes_tool
import rsa_tool
import hashlib
import base64
import re

# ==============================
# WINDOW
# ==============================

root = tk.Tk()
root.title("Text Encryption Tool (AES + RSA)")
root.geometry("1200x800")
root.configure(bg="white")

main = tk.Frame(root, bg="white")
main.pack(expand=True)

TITLE_FONT = ("Segoe UI", 22, "bold")
LABEL_FONT = ("Segoe UI", 12)

private_key_global = None
public_key_global = None
signature_global = None
last_encrypted_text = ""
last_result_text = ""

# ==============================
# HEADER
# ==============================

tk.Label(main, text="TEXT ENCRYPTION TOOL (AES + RSA)",
         font=TITLE_FONT, bg="white", fg="black").pack(pady=15)

tk.Label(main,
         text="Secure Password-Based AES & RSA Encryption System",
         bg="white", fg="black").pack()

# ==============================
# ENCRYPTION TYPE
# ==============================

tk.Label(main, text="Encryption Type:",
         font=LABEL_FONT, bg="white", fg="black").pack(pady=10)

encryption_type = tk.StringVar()

dropdown = ttk.Combobox(main,
                        textvariable=encryption_type,
                        values=["AES (Password-Based)", "RSA (Asymmetric)"],
                        state="readonly",
                        width=30)
dropdown.pack()
dropdown.current(0)

# ==============================
# MESSAGE
# ==============================

tk.Label(main, text="Enter Message:",
         font=LABEL_FONT, bg="white", fg="black").pack(pady=10)

message_entry = tk.Text(main, height=6, width=90,
                        bg="white", fg="black",
                        insertbackground="black")
message_entry.pack()

# ==============================
# PASSWORD
# ==============================

tk.Label(main, text="Enter Password (For AES):",
         font=LABEL_FONT, bg="white", fg="black").pack(pady=10)

pass_frame = tk.Frame(main, bg="white")
pass_frame.pack()

password_entry = tk.Entry(pass_frame, width=40,
                          show="*", bg="white",
                          fg="black", insertbackground="black")
password_entry.pack(side=tk.LEFT, padx=5)

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        eye_btn.config(text="👁")
    else:
        password_entry.config(show="")
        eye_btn.config(text="🙈")

eye_btn = tk.Button(pass_frame, text="👁",
                    command=toggle_password,
                    bg="#4CAF50", fg="white")
eye_btn.pack(side=tk.LEFT)

# ==============================
# PASSWORD STRENGTH
# ==============================

strength_label = tk.Label(main,
                          text="Password Strength:",
                          bg="white", fg="black")
strength_label.pack(pady=5)

def check_password_strength(event=None):
    password = password_entry.get()

    if len(password) < 6:
        strength_label.config(text="Weak 🔴", fg="red")
    elif len(password) >= 6:
        strength_label.config(text="Medium 🟡", fg="orange")

    if (len(password) >= 8 and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[@#$%^&*!]", password)):
        strength_label.config(text="Strong 🟢", fg="green")

password_entry.bind("<KeyRelease>", check_password_strength)

# ==============================
# OUTPUT
# ==============================

tk.Label(main, text="Result Output:",
         font=LABEL_FONT, bg="white", fg="black").pack(pady=10)

output_text = tk.Text(main, height=8, width=90,
                      bg="white", fg="black",
                      insertbackground="black")
output_text.pack()

# ==============================
# KEY GENERATION
# ==============================

def generate_key_from_password(password):
    hashed = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

# ==============================
# TEXT ENCRYPT / DECRYPT
# ==============================

def encrypt_action():
    global private_key_global, public_key_global
    global last_encrypted_text, last_result_text

    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Enter message.")
        return

    output_text.delete("1.0", tk.END)

    if encryption_type.get() == "AES (Password-Based)":
        password = password_entry.get().strip()
        key = generate_key_from_password(password)
        encrypted = aes_tool.encrypt_message(message, key)
        last_encrypted_text = encrypted.decode()
        last_result_text = last_encrypted_text
        output_text.insert(tk.END, last_encrypted_text)

    else:
        private_key_global, public_key_global = rsa_tool.generate_keys()
        encrypted = rsa_tool.encrypt_message(message, public_key_global)
        last_encrypted_text = encrypted.hex()
        last_result_text = last_encrypted_text
        output_text.insert(tk.END, last_encrypted_text)

def decrypt_action():
    global private_key_global

    message = message_entry.get("1.0", tk.END).strip()
    output_text.delete("1.0", tk.END)

    if encryption_type.get() == "AES (Password-Based)":
        try:
            password = password_entry.get().strip()
            key = generate_key_from_password(password)
            decrypted = aes_tool.decrypt_message(message.encode(), key)
            output_text.insert(tk.END, decrypted)
        except:
            messagebox.showerror("Error", "Invalid password or data.")
    else:
        if not private_key_global:
            messagebox.showerror("Error", "No RSA key generated yet.")
            return
        try:
            decrypted = rsa_tool.decrypt_message(
                bytes.fromhex(message),
                private_key_global
            )
            output_text.insert(tk.END, decrypted)
        except:
            messagebox.showerror("Error", "Invalid RSA ciphertext.")

# ==============================
# FILE ENCRYPTION (Binary Safe)
# ==============================

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    password = password_entry.get().strip()
    if not password:
        messagebox.showerror("Error", "Enter password.")
        return

    key = generate_key_from_password(password)

    with open(file_path, "rb") as f:
        file_data = f.read()

    encrypted_data = aes_tool.encrypt_message(file_data, key)

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as f:
        f.write(encrypted_data)

    messagebox.showinfo("Success", f"File encrypted:\n{encrypted_path}")

def decrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if not file_path:
        return

    password = password_entry.get().strip()
    if not password:
        messagebox.showerror("Error", "Enter password.")
        return

    key = generate_key_from_password(password)

    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = aes_tool.decrypt_message(encrypted_data, key)

    original_path = file_path.replace(".enc", "")
    with open(original_path, "wb") as f:
        f.write(decrypted_data)

    messagebox.showinfo("Success", f"File decrypted:\n{original_path}")

# ==============================
# DIGITAL SIGNATURE
# ==============================

def sign_message_action():
    global private_key_global, public_key_global, signature_global

    message = message_entry.get("1.0", tk.END).strip()
    private_key_global, public_key_global = rsa_tool.generate_keys()
    signature_global = rsa_tool.sign_message(message, private_key_global)

    messagebox.showinfo("Success", "Message signed.")

def verify_signature_action():
    message = message_entry.get("1.0", tk.END).strip()

    if not public_key_global or not signature_global:
        messagebox.showerror("Error", "No signature available.")
        return

    valid = rsa_tool.verify_signature(message,
                                      signature_global,
                                      public_key_global)

    if valid:
        messagebox.showinfo("Verified", "Signature VALID ✅")
    else:
        messagebox.showerror("Invalid", "Signature INVALID ❌")

# ==============================
# COPY & SAVE
# ==============================

def copy_text():
    if last_encrypted_text:
        root.clipboard_clear()
        root.clipboard_append(last_encrypted_text)

def save_file():
    if not last_result_text:
        messagebox.showerror("Error", "Nothing to save.")
        return

    with open("encrypted_output.txt", "w") as f:
        f.write(last_result_text)

    messagebox.showinfo("Saved", "Saved to encrypted_output.txt")

# ==============================
# BUTTONS
# ==============================

btn = tk.Frame(main, bg="white")
btn.pack(pady=20)

tk.Button(btn, text="Encrypt", command=encrypt_action,
          bg="#4CAF50", fg="white", width=14).grid(row=0, column=0, padx=5)

tk.Button(btn, text="Decrypt", command=decrypt_action,
          bg="#2196F3", fg="white", width=14).grid(row=0, column=1, padx=5)

tk.Button(btn, text="Encrypt File", command=encrypt_file,
          bg="#673AB7", fg="white", width=14).grid(row=0, column=2, padx=5)

tk.Button(btn, text="Decrypt File", command=decrypt_file,
          bg="#3F51B5", fg="white", width=14).grid(row=0, column=3, padx=5)

tk.Button(btn, text="Sign", command=sign_message_action,
          bg="#795548", fg="white", width=14).grid(row=1, column=0, pady=10)

tk.Button(btn, text="Verify", command=verify_signature_action,
          bg="#607D8B", fg="white", width=14).grid(row=1, column=1)

tk.Button(btn, text="Copy", command=copy_text,
          bg="#FF9800", fg="white", width=14).grid(row=1, column=2)

tk.Button(btn, text="Save", command=save_file,
          bg="#009688", fg="white", width=14).grid(row=1, column=3)

# ==============================
# FOOTER
# ==============================

tk.Label(main,
         text="Developed by Akash Kumar Gupta | Cybersecurity Internship Project 2026",
         bg="white", fg="black").pack(pady=20)

root.mainloop()