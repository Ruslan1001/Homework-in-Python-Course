# Exercise 5:
# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.
# first two terms
n = int(input())
x,y=0,1
while y<=n:
    print(y)
    x,y=y,x+y 

    