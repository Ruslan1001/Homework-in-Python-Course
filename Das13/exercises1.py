# 1. Write a Python program to square and cube every number in a given list of
# integers using Lambda.
numbers=(1,2,3,4,5)
my_sum=list(map(lambda x:x*x,numbers,))
print((my_sum))
sum=list(map(lambda x:x*x*x,numbers))
print((sum))