import os
from cryptography.fernet import Fernet


def load_key():
    """Load the secret key from the 'key.key' file and validate it."""
    if not os.path.exists("key.key"):
        print("Key file not found. Please generate a key first.")
        input("Press Enter to exit...")
        exit()
    with open("key.key", "rb") as file:
        key = file.read()
    try:
        # Check if the key is a valid Fernet key
        Fernet(key)
    except ValueError:
        print("Invalid key detected in 'key.key'. Please generate a new key.")
        os.remove("key.key")
        generate_key()
        key = load_key()
    return key


def generate_key():
    """Generate a new secret key and save it to 'key.key'."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
    print("New key generated and saved to 'key.key'.")


def view_passwords():
    """View all stored passwords."""
    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            try:
                data = line.strip()
                if "|" in data:
                    user, encrypted_pass = data.split("|")
                    decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_pass}")
                else:
                    print("Invalid entry found in the file.")
            except Exception as e:
                print(f"Error decrypting an entry: {e}")


def add_password():
    """Add a new password entry."""
    name = input("Account Name: ").strip()
    if not name:
        print("Account name cannot be empty.")
        return

    pwd = input("Password: ").strip()
    if not pwd:
        print("Password cannot be empty.")
        return

    with open("passwords.txt", "a") as file:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        file.write(name + "|" + encrypted_pwd + "\n")
    print(f"Password for '{name}' added successfully.")\
    
if not os.path.exists("key.key"):
    print("Key file not found. Generating a new key...")
    generate_key()


key = load_key()
fer = Fernet(key)

while True:
    mode = input(
        "\nWould you like to add a new password or view existing ones (view, add), or press q to quit? "
    ).strip().lower()
    if mode == "q":
        print("Goodbye!")
        break
    elif mode == "view":
        view_passwords()
    elif mode == "add":
        add_password()
    else:
        print("Invalid mode. Please enter 'view', 'add', or 'q'.")
