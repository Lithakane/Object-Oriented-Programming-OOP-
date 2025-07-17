class Rectangle:
    """Represents a rectangle shape."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate and return the area."""
        return self.length * self.width


if __name__ == "__main__":
    try:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        rect = Rectangle(length, width)
        print(f"Area: {rect.area()}")
    except ValueError:
        print("Error: Please enter valid numbers")