# Write a Python program to add two given lists using map and
# lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
# ynduni, orinak erku list)
add_two_list=lambda x,y: x+y
num=[1,2,3]
numbers=[4,5,6]
z=list(map(add_two_list,num,numbers))
print(z)