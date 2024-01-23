import requests
import random
import string

'''
Łukasz Lubnar 81449
Lab 3, Zadanie 2
A jednak to nie było takie trudne, gdyż znalazłem prostą stronkę z API słownika, do którego program wysyła zapytanie.
Miało nie być bibliotek, które nie są default i niestety tą bibliotekę requests trzeba doinstalowac 'pip install requests'
także zapisałem to jako plik dodatkowy.
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
print()

def get_dictionary_entry(word):
    api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print(f"Error fetching dictionary entry for '{word}': {response.status_code}")
        return None

print("Making sure your Password is not any word from a Dictionairy (the resulted 404 message means it's not a word):")
dictionary_entry = get_dictionary_entry(secure_password)

if dictionary_entry:
    print("Dictionary Entry:")
    print(dictionary_entry)
