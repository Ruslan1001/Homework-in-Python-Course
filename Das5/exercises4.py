# 4.Second smallest
# Write a Python program to find the second smallest number in a list
list_1=[5,2,10,4]
number=0
for x in list_1:
    if number==0 or x < number:
        number=x
print(number)