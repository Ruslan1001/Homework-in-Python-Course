# Exercise 4:
# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.
import random
random_number=random.randint(1,
 100)

numbers=(input("enter your number"))                 
number=int(input())  
if  number< random_number:
    print("number is less random_number")
number=int(input())  
if number>random_number:
    print(" number is greater random_number")
number=int(input())    
if number==random_number:
    print("number==random_number")
number=int(input())
    
