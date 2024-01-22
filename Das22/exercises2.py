# ● Character Frequency:
# ○ Given a string, create a dictionary where keys are characters and values are their
# frequencies in the string.
string_1 = "abracadabra"
frequency = {k:string_1.count(k) for k in string_1}
print(frequency)