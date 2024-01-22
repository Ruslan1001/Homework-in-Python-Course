# 5.Duplicates
# Write a Python program to remove duplicates from a list
list_1=[1,2,3,1,2,4]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)

