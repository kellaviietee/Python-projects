"""Shapes."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {super().get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {super().get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of shape."""

    def __init__(self, color: str, length: float, width: float):
        """
        Constructor of the rectangle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {super().get_color()})"

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Area of the rectangle is width * height.
        """
        return self.length * self.width


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self,):
        """Constructor should create a list to store all the shapes."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        return self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0.0
        all_shapes = self.get_shapes()
        for shape in all_shapes:
            total_area += shape.get_area()
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        all_shapes = self.get_shapes()
        all_circles = []
        for shape in all_shapes:
            if "Circle" in shape.__repr__():
                all_circles.append(shape)
        return all_circles

    def get_squares(self) -> list:
        """Return only squares."""
        all_shapes = self.get_shapes()
        all_squares = []
        for shape in all_shapes:
            if "Square" in shape.__repr__():
                all_squares.append(shape)
        return all_squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        all_shapes = self.get_shapes()
        all_rectangles = []
        for shape in all_shapes:
            if "Rectangle" in shape.__repr__():
                all_rectangles.append(shape)
        return all_rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
