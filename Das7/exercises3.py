#3.Balance
#Write a program to check if two strings are balanced. For example, strings s1 and
#s2 are balanced if all the characters in the s1 are present in s2. The character’s
#position doesn’t matter.
word_1="world"
world_2="hjvadvkjkjskjrowld"
sum=0
for i  in word_1:
    if i in world_2:
         sum+=1    
if sum==len(word_1):      
     print(True)
else:
      print(False) 