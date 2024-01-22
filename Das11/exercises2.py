#  2.Letters Count 
#Write a Python function to calculate count of each letter in string
def count_letters(str_letter):
    d_1 = {}
    for i in str_letter:
        string_keys = d_1.keys()
        if i in string_keys:
            d_1[i] +=1
        else:
            d_1[i] = 1
    return d_1
print(count_letters("abrakadabra"))