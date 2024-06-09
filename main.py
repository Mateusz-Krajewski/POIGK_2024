from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina import * # pylint: disable=all
from generator import Generator
from gcodeparser import Move

###
SLOWER = 10
###
app =Ursina()

class Game():
    def __init__(self, do) -> None:
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
        self.pomel = Pomel(self.do)
        self.sun = DirectionalLight()
        self.sun.look_at(Vec3(1,-1,-1))
        self.sky = Sky()



    def __pause_input(self, key):
        if key == 'tab':    # press tab to toggle edit/play mode
            self.editor_camera.enabled = not self.editor_camera.enabled

            self.player.visible_self = self.editor_camera.enabled
            self.player.cursor.enabled = not self.editor_camera.enabled
            mouse.locked = not self.editor_camera.enabled
            self.editor_camera.position = self.player.position

            application.paused = self.editor_camera.enabled
        if key == 'q':
            exit()

class Pomel(Entity):
    def __init__(self,do:list[Move], **kwargs):
        self.frames = 0
        self.do = do
        self.il = 0
        super().__init__(model='cube', position=(0.5, 1.15,0.5),
                                    scale=(.1,.1,.1), origin_z=0, color=color.red, on_cooldown=False)
    def update(self):
        if self.frames > 1:
            if len(self.do) > self.il:
                self.set_position(self.do[self.il].get_position())
                if not self.do[self.il].only_move:
                    pos = self.position
                    pos[0] += 0
                    pos[1] -= 0.1
                    pos[2] += 0
                    Entity(model='cube', position=(pos), scale=(1/SLOWER,1/SLOWER,1/SLOWER),color=color.white)
                self.il+=1
            self.frames=0
        self.frames+=1


generator = Generator(SLOWER)


do = generator.GenerateSphere(1,60,80)
Game(do)
app.run()