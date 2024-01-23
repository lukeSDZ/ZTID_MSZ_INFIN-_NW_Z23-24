import base64

'''
Łukasz Lubnar 81449
Lab 3, Zadanie 1
Są dwie funkcje jedna do szyfrowania a druga do odszyfrowywania tegoż.
Wzorowałem się na kodumentacji znalezionej do biblioteki base64.
Dodałem funkcjonalne menu programiku
'''


def encrypt_base64():
    text_to_encrypt = input("Enter the text to encrypt: ")
    
    encrypted_text = base64.b64encode(text_to_encrypt.encode()).decode()
    return encrypted_text

def decrypt_base64(encrypted_text):
    # Decrypting the base64-encoded text
    try:
        original_text = base64.b64decode(encrypted_text).decode()
        return original_text
    except base64.binascii.Error:
        return "Error: Unable to decrypt. Encrypted word is missing."

while True:
    print("Menu:")
    print("1. Encrypt a word")
    print("2. Decrypt the encrypted word")
    print("0. Exit")

    choice = input("Choose an option (0/1/2): ")

    if choice == "0":
        break
    elif choice == "1":
        encrypted_text = encrypt_base64()
        print("Encrypted text:", encrypted_text)
    elif choice == "2":
        if 'encrypted_text' not in locals():
            print("Error: Encrypted word is missing. Please encrypt a word first.")
        else:
            decrypted_text = decrypt_base64(encrypted_text)
            print("Decrypted text:", decrypted_text)
    else:
        print("Error: Invalid choice. Choose 0, 1, or 2.")
