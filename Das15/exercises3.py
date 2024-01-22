#             ● Password Checker:
# ○ Write a function that will get a function string and check if the password is strong
# or not.
# Strong password must contain | One uppercase letter | one special symbol | one
# number
# Length of the password should be 8 or more
# If your password is Strong you will return True. else return False
import string
def checker_password(password):
    uppercase = False
    special_symbol = False
    digit = False
    for char in password:
        if char.isupper():
            uppercase = True
        elif char in string.punctuation:
            special_symbol = True
        elif char.isdigit():
            digit = True

    if uppercase and special_symbol and digit and len(password) >= 8:
        return True
    else:
        return False
user_password = input("Enter your password: ")
if checker_password(user_password):
    print(True)
else:
    print(False)
