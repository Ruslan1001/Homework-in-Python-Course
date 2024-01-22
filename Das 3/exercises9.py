#Append new string in the middle of a given (even number of characters) string
#Example:
#Sample = ‘python’
#new_string = ‘new’
#Expected pytnewhon
word="python"
new_string="new"
result=word[:3]+new_string+word[-3:]
print(result)