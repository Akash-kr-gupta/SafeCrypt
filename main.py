import aes_tool
import rsa_tool

print("="*50)
print("        SafeCrypt")
print("="*50)

print("\nSelect Encryption Type:")
print("1. AES Encryption (Symmetric)")
print("2. RSA Encryption (Asymmetric)")

choice = input("\nChoose option (1/2): ")
message = input("Enter message: ")

if choice == "1":
    key = aes_tool.generate_key()
    encrypted = aes_tool.encrypt_message(message, key)
    decrypted = aes_tool.decrypt_message(encrypted, key)

    print("\n" + "="*50)
    print("            AES ENCRYPTION RESULT")
    print("="*50)
    print("Original Message  :", message)
    print("AES Key           :", key.decode())
    print("Encrypted Text    :", encrypted.decode())
    print("Decrypted Text    :", decrypted)
    print("="*50)

elif choice == "2":
    private_key, public_key = rsa_tool.generate_keys()
    encrypted = rsa_tool.encrypt_message(message, public_key)
    decrypted = rsa_tool.decrypt_message(encrypted, private_key)

    print("\n" + "="*50)
    print("            RSA ENCRYPTION RESULT")
    print("="*50)
    print("Original Message  :", message)
    print("Encrypted Text    :", encrypted)
    print("Decrypted Text    :", decrypted)
    print("="*50)

else:
    print("\nInvalid choice. Please select 1 or 2.")