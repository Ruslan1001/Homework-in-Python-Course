# 13. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements)
def set_function(set1,set2):
    if set1&set2:
        print("Set have common elements")
        return False
    else:
        print("Disjoint sets,no common elements")
        return True
print(set_function({2,3,4,5},{1,2,6,7}))