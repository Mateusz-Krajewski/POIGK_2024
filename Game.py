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
