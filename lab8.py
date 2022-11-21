from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def square():
        pass


class Rectangle(Shape):
    __name__ = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b


class Triangle(Shape):
    __name__ = "Triangle"

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def square(self):
        return abs(1 / 2 * self.base * self.height)


class Circle(Shape):
    __name__ = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return pi * self.radius ** 2


def main():
    shapes = [Rectangle(5, 3), Triangle(4, 5), Circle(7)]
    for shape in shapes:
        print(f"{shape.__name__}'s square = {shape.square()}")


if __name__ == "__main__":
    main()
