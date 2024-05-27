from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina import * # pylint: disable=all
from gcodeparser import GCodeParser, Move # pylint: disable=all

###
SLOWER = 100
###

app = Ursina()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))

editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube',
                                z=-10, color=color.orange, origin_y=-.5, speed=8, collider='box')
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))

pomel = Entity(model='cube', position=(0,0,0),
                            scale=(.2,1,.2), origin_z=-.5, color=color.red, on_cooldown=False)


il = 0
do = []
lastMove= Move()
for i in range(0,1*SLOWER):
    for _ in range (0,1*SLOWER):
        move = Move((lastMove.x+1/SLOWER,i/10,lastMove.z))
        do.append(move)
        lastMove = move
    for _ in range (0,1*SLOWER):
        move = Move((lastMove.x,i/10,lastMove.z+1/SLOWER))
        do.append(move)
        lastMove = move
    for _ in range (0,1*SLOWER):
        move = Move((lastMove.x-1/SLOWER,i/10,lastMove.z))
        do.append(move)
        lastMove = move
    for _ in range (0,1*SLOWER):
        move = Move((lastMove.x,i/10,lastMove.z-1/SLOWER))
        do.append(move)
        lastMove = move


def update():
    global il
    if len(do) > il:
        pomel.position = do[il].get_position()
        Entity(model='cube', position=(pomel.position), scale=(0.1,0.1,0.1),color=color.white)
        il+=1
    pass


# class Enemy(Entity):
#     def __init__(self, **kwargs):
#         super().__init__(parent=shootables_parent, model='cube', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
#         self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
#         self.max_hp = 100
#         self.hp = self.max_hp

#     def update(self):
#         dist = distance_xz(player.position, self.position)
#         if dist > 40:
#             return

#         self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)


#         self.look_at_2d(player.position, 'y')
#         hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
#         # print(hit_info.entity)
#         if hit_info.entity == player:
#             if dist > 2:
#                 self.position += self.forward * time.dt * 5

#     @property
#     def hp(self):
#         return self._hp

#     @hp.setter
#     def hp(self, value):
#         self._hp = value
#         if value <= 0:
#             destroy(self)
#             return

#         self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
#         self.health_bar.alpha = 1

# Enemy()
#enemies = [Enemy(x=x*4) for x in range(4)]


def pause_input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position

        application.paused = editor_camera.enabled
    if key == 'q':
        exit()

pause_handler = Entity(ignore_paused=True, input=pause_input)


sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()

app.run()
