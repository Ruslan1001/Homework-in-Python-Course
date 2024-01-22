# 3.Smallest
# Write a Python program to get the smallest number from a list.
list_1=[5,2,3,4]
number=0
for x in list_1:
    if number==0 or x < number:
        number=x
print(number)
