from cryptography.fernet import Fernet

# Generate Key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Key Generated Successfully!")

# Load Key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt Message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)

    encrypted = f.encrypt(message.encode())

    print("\nEncrypted Message:")
    print(encrypted.decode())

# Decrypt Message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)

    decrypted = f.decrypt(encrypted_message.encode())

    print("\nDecrypted Message:")
    print(decrypted.decode())

while True:

    print("\n===== Encryption Tool =====")
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        message = input("Enter Message: ")
        encrypt_message(message)

    elif choice == "3":
        encrypted_message = input("Enter Encrypted Message: ")
        decrypt_message(encrypted_message)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")