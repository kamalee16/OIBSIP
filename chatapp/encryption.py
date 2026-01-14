from cryptography.fernet import Fernet

# SAME key for server & client
KEY = b'Yg4s2hN9m0nYQ2d9n1r7QK0Qq7z5xwz7R6p5v4U3T2s='

cipher = Fernet(KEY)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(message: bytes) -> str:
    return cipher.decrypt(message).decode()
