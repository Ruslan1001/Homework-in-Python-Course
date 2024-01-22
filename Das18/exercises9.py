# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.
def find_key_maximum_value(dictionary):
    skzbnakan_key=""
    skzbnakan_value=0
    for key in dictionary:
        value=dictionary[key]
        if value>skzbnakan_value:
            skzbnakan_key=key
            skzbnakan_value=value
    return  skzbnakan_key,skzbnakan_value
print(find_key_maximum_value({"arshak":22,"vardan":30,"vaxinak":21,"vardges":29}))