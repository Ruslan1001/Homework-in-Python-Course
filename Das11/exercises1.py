# 1.Max of Three
# Write a Python function to find the Max of three numbers.
def max_of_three(number):
    x=sorted(number,reverse=True)
    return x[0]
print(max_of_three([25,56,24])) 
