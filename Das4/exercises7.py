 #7.Birth year
#The program prompts the user their birth year. Assuming a person’s age
#is a non-negative integer not exceeding 120, output the user’s age or the
#words “Incorrect Year”. The sample outputs assume it’s currently the year
#2016. If you are writing this program during any other year, the correct
#answers may differ. Store the value of the current year in a variable.
birth_year = int(input("Enter your birth year: "))
curent_year =2024
age = curent_year - birth_year
print("Your age is:", age)
if age > 120:
    print("Incorrect Year")
elif age < 0:
    print("Incorrect Year")




