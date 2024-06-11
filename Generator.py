import os
import sys
import math
sys.path.insert(0, os.path.abspath('./code'))

from Move import Move

class Generator():
    """
    Generator class for creating objects ready to be printed by a 3D printer.
    
    Args:
        slower (int): Multiplier for the quantity of elements in the printing part.
        YOFFSET (float): Y position offset for the table to place print on the table.
        XZOFFSET (float): X and Z position offset to centralize print.
    """
    def __init__(self, slower,YOFFSET, XZOFFSET) -> None:
        self.slower = slower
        self.YOFFSET = YOFFSET
        self.XZOFFSET = XZOFFSET

    def GenerateCube(self, a) ->list[Move]:
        """
        Generates a list of moves to create a cube.
        
        Args:
            a (int): Size of the cube.
        
        Returns:
            list[Move]: List of moves to create the cube.
        """
        do = []
        lastMove= Move()
        # Generowanie dolnej ściany
        do = []
        lastMove= Move()
        # Generowanie dolnej ściany
        for i in range(0, a * self.slower):
            for j in range(0, a * self.slower):
                move = Move((i / self.slower,  self.YOFFSET, j / self.slower))
                do.append(move)

        for i in range(0, a * self.slower):
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x + self.XZOFFSET / (2*self.slower),
                                    (i / self.slower)+ self.YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ self.YOFFSET,
                                            lastMove.z + self.XZOFFSET / (self.slower*2)))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x - self.XZOFFSET / (2*self.slower),
                                            (i / self.slower)+ self.YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ self.YOFFSET,
                                                lastMove.z - self.XZOFFSET / (2*self.slower)))
                do.append(move)
                lastMove = move

        # Generowanie górnej ściany
        for i in range(0, a * self.slower + 1):
            for j in range(0, a * self.slower +1):
                move = Move(((i / self.slower), a+self.YOFFSET, j / self.slower))
                do.append(move)

        return do
    def GenerateSphere(self, radius: float,
                            num_layers: int, num_points_per_layer: int) -> list[Move]:
        """
        Generates a list of moves to create a sphere.
        
        Args:
            radius (float): Radius of the sphere.
            num_layers (int): Number of layers in the Y direction.
            num_points_per_layer (int): Number of points per layer in the XZ plane.
        
        Returns:
            list[Move]: List of moves to create the sphere.
        """
        YOFFSET = 1.15
        do = []
        for i in range(num_layers):
            phi = math.pi * (i / (num_layers - 1))  # Ustal phi na podstawie warstwy
            for j in range(num_points_per_layer):
                theta = 2 * math.pi * (j / num_points_per_layer)
                x = radius * math.sin(phi) * math.cos(theta) + self.XZOFFSET
                y = radius * math.cos(phi) + YOFFSET + 1*radius
                z = radius * math.sin(phi) * math.sin(theta) + self.XZOFFSET
                move = Move((x, y, z))
                do.append(move)
        do.reverse()
        return do
