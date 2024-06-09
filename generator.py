from gcodeparser import Move
import math

class Generator():
    def __init__(self, slower) -> None:
        self.slower = slower

    def GenerateCube(self, a) ->list[Move]:
        YOFFSET = 1.15
        do = []
        lastMove= Move()
        # Generowanie dolnej ściany
        for i in range(0, a * self.slower):
            for j in range(0, a * self.slower):
                move = Move((i / self.slower,  YOFFSET, j / self.slower))
                do.append(move)
        for i in range(0, a * self.slower):
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x + a / self.slower, (i / self.slower)+ YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ YOFFSET, lastMove.z + a / self.slower))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x - a / self.slower,(i / self.slower)+ YOFFSET, lastMove.z))
                do.append(move)
                lastMove = move
            for _ in range(0, a * self.slower):
                move = Move((lastMove.x, (i / self.slower)+ YOFFSET, lastMove.z - a / self.slower))
                do.append(move)
                lastMove = move

        # Generowanie górnej ściany
        for i in range(0, a * self.slower + 1):
            for j in range(0, a * self.slower +1):
                move = Move(((i / self.slower), a+YOFFSET, j / self.slower))
                do.append(move)

        return do
    def GenerateSphere(self, radius: float, num_layers: int, num_points_per_layer: int) -> list[Move]:
        YOFFSET = 1.15
        do = []
        for i in range(num_layers):
            phi = math.pi * (i / (num_layers - 1))  # Ustal phi na podstawie warstwy
            for j in range(num_points_per_layer):
                theta = 2 * math.pi * (j / num_points_per_layer)
                x = radius * math.sin(phi) * math.cos(theta) +0.5
                y = radius * math.cos(phi) + YOFFSET+1
                z = radius * math.sin(phi) * math.sin(theta) + 0.5
                move = Move((x, y, z))
                do.append(move)
        do.reverse()
        return do