# Exercise 4: Find Index Function
# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.
def find_element_in_the_list(element):
    list=[1,2,3,4,5]
    if element in list:
        return list.index(element)
    else:
        return -1
print(find_element_in_the_list(2))