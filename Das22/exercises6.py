# Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore
dict_1 = {'_key1': 1, 'key2': 2, 'key3': 3}
dict_2 = {'_key4': 4, 'key5': 5, 'key6': 6}

merged_dict = {k: v for k, v in {**dict_1, **dict_2}.items() if not k[0] == '_'}

print(merged_dict)