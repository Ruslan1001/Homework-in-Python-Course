# 2.Count
# Count all letters, digits, and special symbols from a given string
word="hjssagvkdjfnzdfghskgvdgs2346#214@#%58654#$@##$####"
letters=0
digits=0
symbols=0
for i in word:
    if  90<=(ord(i) >=65 )  or (ord(i) >=97 and ord(i) <=122):
        letters+=1
    elif     ( ord(i) >= 48 and ord(i) <=57 ): 
         digits=digits+1
    if  (ord(i) >=35 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64):       
             symbols=symbols+1 
print(f"tarer= {letters},tiv= {digits}, simvol={symbols}")
        