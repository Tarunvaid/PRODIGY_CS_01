def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_text += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = caesar_encrypt(message, shift)
                print(f"Encrypted message: {result}")
            else:
                result = caesar_decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        
        continue_choice = input("Do you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()
