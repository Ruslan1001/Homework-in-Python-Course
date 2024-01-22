#1.Arrange
#Arrange string characters such that lowercase letters should come first
word = input()
list_1=[]
list_2=[]
for i in word:
    if i.islower():
        list_1.append(i)
        count="".join(list_1)
    else:
        list_2.append(i)
        count_1="".join(list_2)
print(count+count_1)

        
    

       
    
