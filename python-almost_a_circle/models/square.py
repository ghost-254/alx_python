# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents a square with equal width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square (both width and height).
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): Unique identifier for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override __str__ method to return formatted string."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
