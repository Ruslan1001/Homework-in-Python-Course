# Write a program that takes a string as input and counts the
# number of vowels (a, e, i, o, u) in the string. Use a for
# loop, an if statement, and the in operator to check if a
# character is a vowel.
word=input()
vowel_letters="a","e","i","o","u"
count=0
for i in word:
    if i in vowel_letters:
        count+=1
print(count)