# Exercise 5: Sum of Squares Function
# Write a function that calculates the sum of squares of numbers from 1 to n.
def sum_squares_of_numbers(*number):
    result=0
    for i in number:
        result+=i**2
    return result
print(sum_squares_of_numbers(5,5,8,7,9,9,4))