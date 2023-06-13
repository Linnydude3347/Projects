"""
Shape Area and Perimeter Classes - Create an abstract class called Shape and then inherit from it other
shapes like diamond, rectangle, circle, triangle etc. Then have each class override the area and perimeter
functionality to handle each shape type.

https://github.com/karan/Projects
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

class Triangle(Shape):

    def __init__(self, s1: int, s2: int, s3: int) -> None:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self) -> int | float:
        s = (self.s1 + self.s2 + self.s3) / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    
    def perimeter(self) -> int:
        return self.s1 + self.s2 + self.s3

class Square(Shape):

    def __init__(self, s1: int, s2: int, s3: int, s4: int) -> None:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
    
    def area(self) -> int:
        return self.s1 * self.s2

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4