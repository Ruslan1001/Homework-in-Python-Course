# Write a program that prompts the user to enter a word and checks if it is
# a palindrome. A palindrome is a word that reads the same backward as
# forward. Use string slicing and an if-else statement to compare the
# original word with its reverse.
word=input("enter your word ")
if word[:3]==word[-1]+word[-2]+word[-3]:
    print("word is palindrome")
else:
    print("word is not palindrome")