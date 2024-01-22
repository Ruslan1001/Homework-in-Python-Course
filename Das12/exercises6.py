# Exercise 6: Count Words Function
# Write a function that counts the number of words in a sentence.
def count_words_in_sentence(sentence):  
    for i in  sentence:
        result=sentence.split()
        words=len(result)
    return words
print(count_words_in_sentence("Python is the programming language "))