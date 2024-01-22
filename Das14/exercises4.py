# 4.Write a function display_words() in python to read text from a text file "example.txt",
# and display those words, which are less than 4 characters.
with open("text_1.txt","r") as file:
    y=file.read()
    list_1=[]
    z=y.split()
    for i in z:
        if len(i)<4:
            list_1.append(i)
print(list_1)
        