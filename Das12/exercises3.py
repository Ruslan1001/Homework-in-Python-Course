#Exercise 3: Average Function
#Write a function that calculates the average of a list of numbers.
def average_of_list_numbers(number):
    result=0
    x=0
    for i in number:
        result+=i
        x+=1
    return result/x  
print( average_of_list_numbers([20,20,29]))