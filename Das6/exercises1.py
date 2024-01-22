# Exercise 1: Counting Even Numbers
# Write a program that takes a list of numbers as input and
# counts the number of even numbers in the list. Use a for
# loop, an if statement, and the modulus operator (%) to
# determine if a number is even or odd
list1 =[1,3,4,5,6]
even_count=0
for i in list1:
    if i%2==0:
        even_count+=1
print("Even number is",even_count)

