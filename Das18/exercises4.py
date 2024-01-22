# 4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)
def two_list_return_new_list(list_1,list_2):
    new_list=[]
    for i in list_1:
        if i in list_2:
            new_list.append(i)
        else:
            i+=1
    return new_list
print(two_list_return_new_list([1,2,3,10,4,5],[1,4,5,10,6,3]))