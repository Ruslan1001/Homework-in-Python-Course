# 3.Factorial
# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(n):
    y=1
    for i in range(2,n+1):
        y*=i
    return y
print(factorial(5))
