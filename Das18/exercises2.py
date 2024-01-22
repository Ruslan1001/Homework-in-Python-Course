# 2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.
class Calculator: 
    def addition(self,number_1,number_2):
        return number_1+number_2
    def subtraction(self,number1,number2):
        return number1-number2
    def multiplication(self,num1,num2):
        return num1*num2
    def devision(self,num1,num2):
        if num2!=0:
            return num1/num2
        else:
            raise ZeroDivisionError("num2=0")
        
bacic_calculator=Calculator()     
x=bacic_calculator.addition(20,20)
print(x)
y=bacic_calculator.subtraction(100,10)
print(y)
v=bacic_calculator.multiplication(5,7)
print(v)
z=bacic_calculator.devision(25,5)
print(z)