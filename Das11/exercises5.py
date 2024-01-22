# 2.Write a python program which concat 2 dicts.
dict_1={"a":5,"b":4}
dict_2={"c":10,"d":20}
for k,v in dict_2.items():
    if k not in dict_1:
        dict_1[k]=v
print(dict_1)