import random
import string

'''
Łukasz Lubnar 81449
Lab 3, Zadanie 2
Funkcja kreująca zaszyfrowane hasło. 
Długość hasła jest zdefiniowana poprzez zmienną random_number i na ten moment jest od 8 do 20 znaków, oczywiście można wstawić dowolny górny limit. 
Generalnie brakuje elementu który sprawdzi czy słowo nie znajduje się w słowniku.
Myślę, że można było by zapytać jakieś słownikowe API, ale już nie wyrabiam się czasowo, żeby poszukać takiego i wczytać się.
'''


def generate_secure_password():

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    print("Those are the characters allowed: ", all_characters)
    print()

    random_number = random.randint(8, 20)
    while True:
        password = ''.join(random.choice(all_characters) for _ in range(random_number)) 

        if (any(char.isupper() for char in password) and
                any(char.islower() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in special_characters for char in password) and
                len(password) >= 8):
            return password


secure_password = generate_secure_password()
print("This is your secure Password:", secure_password)
