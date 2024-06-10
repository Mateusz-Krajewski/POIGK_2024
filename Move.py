class Move:
    """
    Represents a move in GCode.
    
    Args:
        position (tuple, optional): The (x, y, z) coordinates of the move. Defaults to (0, 0, 0).
        only_move (bool, optional): Flag indicating if the move is only a movement. Defaults to False.
    """

    def __init__(self, position=(0, 0, 0), only_move=False):
        self.x: float = position[0]
        self.y: float = position[1]
        self.z: float = position[2]
        self.only_move = only_move

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}, OnlyMove: {self.only_move}"

    def get_position(self):
        """
        Get the current position as a tuple.

        Returns:
            tuple: The (x, y, z) coordinates of the move.
        """
        return self.x, self.y, self.z

    def change_x(self, delta_x):
        """
        Change the X coordinate by delta_x.

        Args:
            delta_x (float): The amount to change the X coordinate by.
        """
        self.x += delta_x

    def change_y(self, delta_y):
        """
        Change the Y coordinate by delta_y.

        Args:
            delta_y (float): The amount to change the Y coordinate by.
        """
        self.y += delta_y

    def change_z(self, delta_z):
        """
        Change the Z coordinate by delta_z.

        Args:
            delta_z (float): The amount to change the Z coordinate by.
        """
        self.z += delta_z
