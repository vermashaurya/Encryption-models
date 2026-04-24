def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypts or decrypts text using Caesar Cipher.
    """
    if decrypt:
        shift = -shift
        
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

if __name__ == '__main__':
    while True:
        print("\n--- Caesar Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (0-25): "))
            ciphertext = caesar_cipher(plaintext, shift)
            print(f"Encrypted text: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (0-25): "))
            decrypted_text = caesar_cipher(ciphertext, shift, decrypt=True)
            print(f"Decrypted text: {decrypted_text}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
