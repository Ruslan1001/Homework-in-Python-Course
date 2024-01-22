# Exercise 9: Print Prime Numbers Function
# Write a function that prints all prime numbers up to a given limit.
def print_prime_numbers(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list:
    if i > 1 and print_prime_numbers(i):
        print(i)