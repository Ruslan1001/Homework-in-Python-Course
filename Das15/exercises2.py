#       Random Password Generator:
# Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols).
import random
import string
def generate_random_password(length, letters=True, numbers=True, symbols=True):
    letters = string.ascii_letters 
    numbers = string.digits 
    symbols = string.punctuation 
    all_characters = letters + numbers + symbols
    password = ''.join(random.choice(all_characters) for i in range(password_length))
    return password

password_length = int(input("Enter the lenght of password: "))
random_password = generate_random_password(password_length)
print("Your Password:", random_password)




