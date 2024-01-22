# 3. List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.
def sum_numbers_divided_7(number):
    result=0
    for i in number:
        if i%7==0:
            result+=i
    return result
print(sum_numbers_divided_7([7,28,49,5,6,8,63]))
