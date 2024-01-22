#3.Digit Sum
#Input a two-digit natural number and output the sum of its digits. You can
#assume that the input will be a two-digit number and need not check that 
#programmatically.
number=int(input())
x=number%10
y=number//10
print(x+y)