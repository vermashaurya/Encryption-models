def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_cipher(text, key, decrypt=False):
    key = generate_key(text, key).upper()
    text = text.upper()
    result = []
    
    for i in range(len(text)):
        if text[i].isalpha():
            if decrypt:
                x = (ord(text[i]) - ord(key[i]) + 26) % 26
            else:
                x = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
            x += ord('A')
            result.append(chr(x))
        else:
            result.append(text[i])
            
    return "".join(result)

if __name__ == "__main__":
    while True:
        print("\n--- Vigenère Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            text = input("Enter the string to encrypt (letters only recommended): ")
            keyword = input("Enter the keyword: ")
            cipher_text = vigenere_cipher(text, keyword)
            print(f"Ciphertext: {cipher_text}")
        elif choice == "2":
            text = input("Enter the ciphertext to decrypt: ")
            keyword = input("Enter the keyword: ")
            original_text = vigenere_cipher(text, keyword, decrypt=True)
            print(f"Original/Decrypted Text: {original_text}")
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please select a valid option.")
