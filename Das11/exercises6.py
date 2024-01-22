# 3.Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers
def numbers_cube():
    number=int(input())
    my_dict={}
    for i in range(1,number+1):
        my_dict[i]=i**3
    print(my_dict)
numbers_cube()