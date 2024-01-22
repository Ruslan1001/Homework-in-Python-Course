#8.Three Numbers
#Input three integers. Output the word “Sorted” if the numbers are listed in
#a non-increasing or non-decreasing order and “Unsorted” otherwise.
x=int(input())
y=int(input())
z=int(input())
if x<y<z:
  if x>y>z:
    print("unsorted")
else:
  print("sorted")