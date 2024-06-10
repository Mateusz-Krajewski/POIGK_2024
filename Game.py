import os
import sys
import random

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

sys.path.insert(0, os.path.abspath('./code'))


from Pomel import Pomel
from Generator import Generator

class Game():
    """
    Main class of the game. Initializes the ground, table, player, camera,
    player collision, key press handler, sun, and opens the menu.

    Args:
        slower (int): Multiplier for the quantity of elements in the printing part.
        YOFFSET (float): Y position offset for the table to place print on the table.
        XZOFFSET (float): X and Z position offset to centralize print.
    """
    def __init__(self, slower,YOFFSET, XZOFFSET) -> None:
        self.slower = slower
        self.do = []
        self.gen = Generator(slower, YOFFSET, XZOFFSET)
        random.seed(0)
        self.app = Ursina()
        Entity.default_shader = lit_with_shadows_shader
        self.ground = Entity(model='plane', collider='box',
                                    scale=64, texture='grass', texture_scale=(4,4))
        self.table = Entity(model='plane', collider='box',
                                    color=color.gray,position=(1,1,1),scale=(8,0.1,8))

        self.editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self.player = FirstPersonController(model='cube', z=-10, color=color.orange,
                                                origin_y=-0.5, speed=8, collider='box')
        self.player.collider = BoxCollider(self.player, Vec3(0,1,0), Vec3(1,2,1))
        self.pause_handler = Entity(ignore_paused=True, input=self.pause_input)
        self.sun = DirectionalLight()
        self.sun.look_at(Vec3(1,-1,-1))
        self.sky = Sky()
        self.pomel = None
        self.menu_is_on =False
        self.menu()
        self.app.run()

    def Cursor(self):
        """
        Toggles the player cursor, allowing the player to choose a position
        from the menu or move the camera.
        """
        self.editor_camera.enabled = not self.editor_camera.enabled
        self.player.visible_self = self.editor_camera.enabled
        mouse.locked = not self.editor_camera.enabled
        self.editor_camera.position = self.player.position

    def menu(self):
        """
        Displays the menu, prints buttons and input fields.
        """
        if (not self.menu_is_on):
            self.Cursor()
            self.gen_cube_but = Button(
                color = color.gray,
                y = 0.1,
                scale = (.1,.1),
                text="Cube",
                on_click=self.start_gen_cube,
            )
            self.gen_cube_a_but = InputField(
                text="Cube Size",
                active=False,
                y = 0,
                default_value='1',
            )
            self.gen_sphere_but = Button(
                color = color.gray,
                y = -0.1,
                scale = (.1,.1),
                text="Sphere",
                on_click=self.start_gen_sphere,
            )
            self.gen_sphera_r_but = InputField(
                text="Radius of Sphare",
                active=False,
                y = -0.2,
                default_value='1',
            )
            self.gen_sphera_line_but = InputField(
                active=False,
                y = -0.3,
                default_value='20',
            )
            self.gen_sphera_a_but = InputField(
                active=False,
                y = -0.4,
                default_value='40',
            )
            self.menu_is_on = True
        else:
            self.unpauseBase()
            self.pomel.enable()
            self.pomel.enableEntity()

    def unpauseBase(self):
        """
        Disables menu buttons, enables the cursor.
        """
        self.gen_cube_but.disable()
        self.gen_sphere_but.disable()
        self.gen_cube_a_but.disable()
        self.gen_sphera_r_but.disable()
        self.gen_sphera_line_but.disable()
        self.gen_sphera_a_but.disable()
        self.Cursor()
        self.menu_is_on = False

    def start_gen_cube(self):
        """
        Reads data from menu fields and generates a cube with the given arguments.
        """
        a = int(self.gen_cube_a_but.text)
        do = self.gen.GenerateCube(a)
        self.pomel = Pomel(do,slower=self.slower)
        self.unpauseBase()

    def start_gen_sphere(self):
        """
        Reads data from menu fields and generates a sphere with the given arguments.
        """
        do = self.gen.GenerateSphere(int(self.gen_sphera_r_but.text),int(self.gen_sphera_line_but.text), int(self.gen_sphera_a_but.text))
        self.pomel = Pomel(do,slower=self.slower)
        self.unpauseBase()

    def pause_input(self, key):
        """
        Callback for pressed keyboard keys:
        - 'q' - Quit the game.
        - 'r' - Remove object from table and Pomel.
        - 'm' - Pause printing and open menu; second press unpauses printing.
        - 'p' - Pause/Unpause printing.

        Args:
            key (str): Name of the pressed key.
        """
        if key == 'q':
            exit()
        if key == 'r':
            self.pomel.dropEntity()
            self.pomel.disable()
        if key == 'm':
            if self.pomel is not None:
                self.pomel.dropEntity()
                self.pomel.disable()
            self.menu()
        if key == "p":
            self.pomel.ChangePause()
