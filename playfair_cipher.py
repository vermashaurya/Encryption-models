import string

def create_matrix(keyword):
    keyword = keyword.lower().replace('j', 'i')
    alphabet = string.ascii_lowercase.replace('j', '')
    matrix = list()
    for char in keyword:
        if char not in matrix and char.isalpha():
            matrix.append(char)
            
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
            
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return -1, -1

def playfair_cipher(text, keyword, decrypt=False):
    matrix = create_matrix(keyword)
    text = text.lower().replace('j', 'i')
    
    # Filter out non-alphabetic characters
    clean_text = "".join([c for c in text if c.isalpha()])
    
    pairs = []
    i = 0
    while i < len(clean_text):
        if i == len(clean_text) - 1 or clean_text[i] == clean_text[i + 1]:
            pairs.append(clean_text[i] + 'x')
            i += 1
        else:
            pairs.append(clean_text[i:i + 2])
            i += 2
            
    result = ''
    shift = -1 if decrypt else 1
    
    for pair in pairs:
        c1, c2 = pair[0], pair[1]
        r1, col1 = find_position(c1, matrix)
        r2, col2 = find_position(c2, matrix)
        
        if r1 == r2:
            result += matrix[r1][(col1 + shift) % 5]
            result += matrix[r2][(col2 + shift) % 5]
        elif col1 == col2:
            result += matrix[(r1 + shift) % 5][col1]
            result += matrix[(r2 + shift) % 5][col2]
        else:
            result += matrix[r1][col2]
            result += matrix[r2][col1]
            
    if decrypt:
        result = result.replace('x', '')
        
    return result

if __name__ == '__main__':
    while True:
        print("\n--- Playfair Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter the plain text: ")
            keyword = input("Enter the keyword: ")
            cipher_text = playfair_cipher(text, keyword)
            print(f"Cipher Text: {cipher_text}")
        elif choice == '2':
            text = input("Enter the cipher text: ")
            keyword = input("Enter the keyword: ")
            plain_text = playfair_cipher(text, keyword, decrypt=True)
            print(f"Plain Text: {plain_text}")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")
