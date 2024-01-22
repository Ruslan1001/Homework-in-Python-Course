#  Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.
list_1=["program","python","is","the","of"]
dict_1={k:len(k) for k in list_1  if len(k)>3 }
print(dict_1)