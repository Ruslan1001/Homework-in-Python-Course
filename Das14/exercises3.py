#3. Write a python program to add text to a file and display the text in python.txt
with open("text.txt","a") as file:
    print(file.write("\npython is the programming language"))
with open("text.txt","r") as file:
    print(file.read())
print(file.closed)