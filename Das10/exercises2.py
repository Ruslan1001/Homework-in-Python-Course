# Exercise 2:
# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user
real_password="bdg2023"
password=input()
while password != real_password:
    print('false password')
    password=input()
if password==real_password:
    print("real password,password is this")
