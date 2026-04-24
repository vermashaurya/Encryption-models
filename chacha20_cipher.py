from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_chacha20_fernet(plaintext, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(plaintext.encode())

def decrypt_chacha20_fernet(ciphertext, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(ciphertext).decode()

if __name__ == "__main__":
    print("\n--- Fernet (AES/ChaCha20 equivalent) Cipher ---")
    key = generate_key()
    print(f"Generated Key (Keep Secret): {key.decode()}")
    
    plaintext = input("Enter text to encrypt: ")
    ciphertext = encrypt_chacha20_fernet(plaintext, key)
    print(f"\nCiphertext: {ciphertext.decode()}")
    
    decrypted = decrypt_chacha20_fernet(ciphertext, key)
    print(f"Decrypted: {decrypted}")
