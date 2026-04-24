def rail_fence_cipher(text, rails, decrypt=False):
    if rails <= 1 or rails >= len(text):
        return text
        
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    dir_down = False
    row, col = 0, 0

    if not decrypt:
        for i in range(len(text)):
            if row == 0 or row == rails - 1:
                dir_down = not dir_down
            fence[row][col] = text[i]
            col += 1
            row += 1 if dir_down else -1
            
        result = []
        for i in range(rails):
            result.extend([fence[i][j] for j in range(len(text)) if fence[i][j] != '\n'])
        return ''.join(result)
    else:
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            fence[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1
            
        index = 0
        for i in range(rails):
            for j in range(len(text)):
                if fence[i][j] == '*' and index < len(text):
                    fence[i][j] = text[index]
                    index += 1
                    
        result = []
        row, col = 0, 0
        for _ in range(len(text)):
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False
            if fence[row][col] != '*':
                result.append(fence[row][col])
            col += 1
            row += 1 if dir_down else -1
            
        return ''.join(result)

if __name__ == "__main__":
    while True:
        print("\n--- Rail Fence Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the plain text: ")
            rails = int(input("Enter the number of rails: "))
            cipher_text = rail_fence_cipher(text, rails)
            print(f"Cipher Text: {cipher_text}")
        elif choice == '2':
            text = input("Enter the cipher text: ")
            rails = int(input("Enter the number of rails: "))
            plain_text = rail_fence_cipher(text, rails, decrypt=True)
            print(f"Decrypted Text: {plain_text}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
