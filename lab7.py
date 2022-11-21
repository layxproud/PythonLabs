import math


class MyVector:
    """Vector2D realization"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Correct vector representation"""
        return f"<{self.x}; {self.y}>"

    def __str__(self):
        """Correct vector representation"""
        return f"<{self.x}; {self.y}>"

    def __add__(self, other):
        """Vector sum"""
        print(MyVector(self.x + other.x, self.y + other.y))

    def __eq__(self, other):
        """Vector equality"""
        if self.__abs__() == other.__abs__():
            print("YES")
        else:
            print("NO")

    def __mul__(self, other):
        """Vector multiplication"""
        if type(other) is MyVector:
            print(MyVector(self.x * other.x, self.y * other.y))
        else:
            print(MyVector(self.x * other, self.y * other))

    def __abs__(self):
        """Vector length"""
        return math.sqrt(self.x ** 2 + self.y ** 2)


def main():
    """Main function"""
    vector1 = MyVector(1, 2)
    vector2 = MyVector(3, 4)

    print("First vector:", end=" ")
    print(vector1)

    print("Second vector:", end=" ")
    print(vector2)

    print(f"Vector {vector1} + vector {vector2} = ", end=" ")
    vector1 + vector2

    print(f"Is vector {vector1} equal to vector {vector2}?", end=" ")
    vector1 == vector2

    print(f"Vector {vector1} * 3 = ", end=" ")
    vector1 * 3

    print(f"Vector {vector1} * vector {vector2} =", end=" ")
    vector1 * vector2

    print(f"Length of vector {vector1} is", end=" ")
    print(vector1.__abs__())


if __name__ == "__main__":
    main()
