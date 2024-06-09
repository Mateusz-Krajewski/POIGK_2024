import random
from ursina import Entity, color, Ursina, BoxCollider, Vec3, DirectionalLight, Sky, EditorCamera, mouse, application
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

from Pomel import Pomel

class Game():
    def __init__(self, do, slower) -> None:
        """Main class Of the game, they initialize all of Entities

        Args:
            do (list[Move]): list of moves to get by Pomel class
            slower (int): multiply quantity of elements in printing part
        """
        self.slower = slower
        self.do = do
        random.seed(0)
        self.app = Ursina()
        Entity.default_shader = lit_with_shadows_shader
        self.ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
        self.table = Entity(model='plane', collider='box', color=color.gray,position=(0.5,1,0.5),scale=(2,0.1,2))

        self.editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self.player = FirstPersonController(model='cube',
                                        z=-10, color=color.orange, origin_y=-0.5, speed=8, collider='box')
        self.player.collider = BoxCollider(self.player, Vec3(0,1,0), Vec3(1,2,1))
        self.pause_handler = Entity(ignore_paused=True, input=self.__pause_input)
        self.pomel = Pomel(self.do,slower)
        self.sun = DirectionalLight()
        self.sun.look_at(Vec3(1,-1,-1))
        self.sky = Sky()
        self.app.run()



    def __pause_input(self, key):
        """Callback of enter keyboard key, allow to pause symulation or exit the game

        Args:
            key (str): string name of pressed key
        """
        if key == 'tab':    # press tab to toggle edit/play mode
            self.editor_camera.enabled = not self.editor_camera.enabled

            self.player.visible_self = self.editor_camera.enabled
            self.player.cursor.enabled = not self.editor_camera.enabled
            mouse.locked = not self.editor_camera.enabled
            self.editor_camera.position = self.player.position

            application.paused = self.editor_camera.enabled
        if key == 'q':
            exit()

from Move import Move
from ursina import color, Entity

class Pomel(Entity):
    """Pomel class is responsible for Move Pomel Model and Generate printing efect

    Args:
        do: (list[Move]): moves lists
    """
    def __init__(self,do:list[Move],slower, **kwargs):
        self.frames = 0
        self.do = do
        self.il = 0
        self.slower = slower
        super().__init__(model='cube', position=(0.5, 1.15,0.5),
                                    scale=(.1,.1,.1), origin_z=0, color=color.red, on_cooldown=False)
    def update(self):
        """Function called by ursina engine. They change position of Pomel and print Cube
        """
        if self.frames > 1:
            if len(self.do) > self.il:
                self.set_position(self.do[self.il].get_position())
                if not self.do[self.il].only_move:
                    pos = self.position
                    pos[0] += 0
                    pos[1] -= 0.1
                    pos[2] += 0
                    Entity(model='cube', position=(pos), scale=(1/self.slower,1/self.slower,1/self.slower),color=color.white)
                self.il+=1
            self.frames=0
        self.frames+=1
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

from Move import Move
import math

class Generator():
    """Generator Objects Ready to print by 3D Priner
    """
    def __init__(self, slower) -> None:
        self.slower = slower

    def GenerateCube(self, a) ->list[Move]:
        """Function generates Moves to create Cube 

        Args:
            a (int): size of Cube

        Returns:
            list[Move]: moves list
        """
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
                x = radius * math.sin(phi) * math.cos(theta) +0.5
                y = radius * math.cos(phi) + YOFFSET+1
                z = radius * math.sin(phi) * math.sin(theta) + 0.5
                move = Move((x, y, z))
                do.append(move)
        do.reverse()
        return do
from Generator import Generator
from Game import Game

###
SLOWER = 10
###

if __name__ == "__main__":
    generator = Generator(SLOWER)
    do = generator.GenerateSphere(1,60,80)
    game = Game(do, SLOWER)
