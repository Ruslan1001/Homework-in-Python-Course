# Write an abstract class with name GeometricFigure
# Write 2 geometric figure classes by inheriting from GeometricFigure
# Write 2 functions
# get_perimeter -> return perimeter of figure
# get_area -> return area of figure
from abc import ABC,abstractmethod
class GeometricFigure(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass
    def get_area(self):
        pass
class Triangle(GeometricFigure):
    def __init__(self,perimeter,area):
        self.perimeter=perimeter
        self.area=area
    def get_perimeter(self):
        return f"Triangle perimeter is {self.perimeter}"
    def get_area(self):
        return f"Triangle area is {self.area}"
triangle=Triangle("a+b+c","to the product of base and height")
print(triangle.get_perimeter())
print(triangle.get_area())
class Square(GeometricFigure):
    def __init__(self,perimeter,area):
        self.perimeter=perimeter
        self.area=area
    def get_perimeter(self):
        return f"Square perimeter is {self.perimeter}"
    def get_area(self):
        return f"Square area is {self.area}"
square=Square("4a","S=a**2")
print(square.get_perimeter())
print(square.get_area())