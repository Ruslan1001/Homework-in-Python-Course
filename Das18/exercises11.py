# 11. Function Exercise:
# Write a function that checks if a given string is a valid email address.
def check_email_addres(str_1):
    str_1 = str_1.replace('.','@')
    str_2 = str_1.split('@')
    if len(str_2) == 3:
        return True
    return False
print(check_email_addres('a-z@.a-z'))