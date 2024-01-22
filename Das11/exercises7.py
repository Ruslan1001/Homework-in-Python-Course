# 4.Write a python function which create dict from 2
# lists with the same length
def create_dict_is_two_lists(k,v):
    dict_1={}
    for i in range(len(k)):
        dict_1[k[i]] = v[i]
    return dict_1

list_1 = ['a', 'b', 'c',]
list_2 = [1, 2, 3,]

dict_1 = create_dict_is_two_lists(list_1, list_2)
print(dict_1)