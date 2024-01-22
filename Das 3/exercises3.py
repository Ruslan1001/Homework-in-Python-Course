# 3. Write a Python program to remove the n-th index character from a nonempty string.
# Example:
# Sample string: ‘abcdefgh’
# n - 3
# Expected result: abcefgh
word=input("enter your word ")
n=int(input())
result=word[:n]+word[n+1:]
print(result)