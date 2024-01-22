# 1.Write a function in python to read the content from a text file "example.txt" line by line
# and display the same on screen.
def read_content_line_by_line():
    with open ("text_2.txt","r") as file:
        y=file.read()
        z=y.split("\n")
        for i in z:
            print(i)  
read_content_line_by_line()