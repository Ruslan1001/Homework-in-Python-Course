#Exercise 5:
#You are given three lists, list1, list2, and list3. Your task is to implement a
#programm that takes these lists and prints the following:
#The set of elements that are common to all three lists.
#The set of elements that are present in at least two of the three lists, but not in all
#three.
#The set of elements that are unique to each list (present in only one list).
list_1 = set('mek')
list_2 = set('erku')
list_3 = set('ereq')
common_elements = list_1 & list_2 & list_3
print(common_elements)

two_or_more_elements = (list_1 & list_2) | (list_1 & list_3) | (list_2 & list_3)

two_or_more_elements -= common_elements
print(two_or_more_elements)

unique_elements_list1 = list_1 - (list_2 | list_3)
unique_elements_list2 = list_2 - (list_1 | list_3)
unique_elements_list3 = list_3 - (list_1 | list_2)
print(unique_elements_list1 | unique_elements_list2 | unique_elements_list3)