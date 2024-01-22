# 4. Write a Python program to change a given string to a new string where the first and last chars
# have been exchanged.
# Example:
# Sample: ‘abcdefgh’
# Expected: ‘hbcdefga’
word=input("enter your word ")
result=word[-1] + word[1:-1]+word[0]
print(result)