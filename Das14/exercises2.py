#2. Write a function in Python to count and display the total number of words in a text file.
def count_words_in_file():
  with open("text.txt","r") as file:
   y=file.read()
   z=y.split()
   v=len(z)
   return z,v
print(count_words_in_file())

