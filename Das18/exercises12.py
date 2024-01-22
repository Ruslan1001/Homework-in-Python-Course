# 12. List Exercise:
# Write a function that returns the nth largest element from a list.
def return_nth_largest_element():
    list_1=[1,2,5,4,3]
    v=sorted(list_1,reverse=True)
    n=3
    x=v[n-1]
    print(x)
return_nth_largest_element()