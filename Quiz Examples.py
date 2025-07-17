from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class RightPyramid(Shape):
    """Represents a right pyramid shape."""

    def __init__(self, base: float, slant_height: float):
        self.base = base
        self.slant_height = slant_height

    def area(self) -> float:
        """Calculate total surface area."""
        base_area = self.base ** 2
        perimeter = 4 * self.base
        return 0.5 * perimeter * self.slant_height + base_area

    def perimeter(self) -> float:
        """Calculate base perimeter."""
        return 4 * self.base