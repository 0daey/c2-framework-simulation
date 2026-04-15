# encryption.py
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    key = generate_key()
    data = "Hello, world!"
    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted data: {encrypted_data}")
    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Decrypted data: {decrypted_data}")