class Move:
    """Represents a move in GCode."""

    def __init__(self, position=(0, 0, 0), only_move=False):
        """Initialize Move with position and only_move flag."""
        self.x: float = position[0]
        self.y: float = position[1]
        self.z: float = position[2]
        self.only_move = only_move

    def __str__(self) -> str:
        """Return string representation of the move."""
        return f"x: {self.x}, y: {self.y}, z: {self.z}, OnlyMove: {self.only_move}"

    def get_position(self):
        """Get the current position as a tuple."""
        return self.x, self.y, self.z

    def change_x(self, delta_x):
        """Change the X coordinate by delta_x."""
        self.x += delta_x

    def change_y(self, delta_y):
        """Change the Y coordinate by delta_y."""
        self.y += delta_y

    def change_z(self, delta_z):
        """Change the Z coordinate by delta_z."""
        self.z += delta_z

