import os
import sys
import math
sys.path.insert(0, os.path.abspath('./code')) 

from Move import Move

class Generator():
    """Generator Objects Ready to print by 3D Priner
    """
    def __init__(self, slower,YOFFSET, XZOFFSET) -> None:
        self.slower = slower
        self.YOFFSET = YOFFSET
        self.XZOFFSET = XZOFFSET

    def GenerateCube(self, a) ->list[Move]:
        """Function generates Moves to create Cube 

        Args:
            a (int): size of Cube

        Returns:
            list[Move]: moves list
        """
        do = []
        lastMove= Move()
        # Generowanie dolnej ściany
        for i in range(0, a * self.slower):
            for j in range(0, a * self.slower):
                move = Move((i / self.slower,  self.YOFFSET, j / self.slower))
                do.append(move)

        for i in range(0, a * self.slower):
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x + self.XZOFFSET / self.slower, (i / self.slower)+ self.YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ self.YOFFSET, lastMove.z + self.XZOFFSET / self.slower))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x - self.XZOFFSET / self.slower,(i / self.slower)+ self.YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ self.YOFFSET, lastMove.z - self.XZOFFSET / self.slower))
                do.append(move)
                lastMove = move

        # Generowanie górnej ściany
        for i in range(0, a * self.slower + 1):
            for j in range(0, a * self.slower +1):
                move = Move(((i / self.slower), a+self.YOFFSET, j / self.slower))
                do.append(move)

        return do
    def GenerateSphere(self, radius: float, num_layers: int, num_points_per_layer: int) -> list[Move]:
        """Function to generate Moves list to create a Sphare

        Args:
            radius (float): radius of sphere
            num_layers (int): nomber of layers in Y
            num_points_per_layer (int): num of points in layer XZ

        Returns:
            list[Move]: moves list
        """
        YOFFSET = 1.15
        do = []
        for i in range(num_layers):
            phi = math.pi * (i / (num_layers - 1))  # Ustal phi na podstawie warstwy
            for j in range(num_points_per_layer):
                theta = 2 * math.pi * (j / num_points_per_layer)
                x = radius * math.sin(phi) * math.cos(theta) + self.XZOFFSET
                y = radius * math.cos(phi) + YOFFSET+1
                z = radius * math.sin(phi) * math.sin(theta) + self.XZOFFSET
                move = Move((x, y, z))
                do.append(move)
        do.reverse()
        return do