from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina import * # pylint: disable=all
from gcodeparser import GCodeParser, Move # pylint: disable=all

###
SLOWER = 10
###


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

app = Ursina()

random.seed(0)
Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
table = Entity(model='plane', collider='box', color=color.gray,position=(0.5,1,0.5),scale=(2,0.1,2))

editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube',
                                z=-10, color=color.orange, origin_y=-0.5, speed=8, collider='box')
#player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))

pomel = Entity(model='cube', position=(0.5, 1.15,0.5),
                            scale=(.1,.1,.1), origin_z=0, color=color.red, on_cooldown=False)


il = 0
frames = 0
gen = Generator(SLOWER)
do = gen.GenerateSphere(1,60,80)

def update():
    global frames
    if frames > 1:
        global il
        if len(do) > il:
            pomel.set_position(do[il].get_position())
            if not do[il].only_move:
                pos = pomel.position
                pos[0] += 0
                pos[1] -= 0.1
                pos[2] += 0
                Entity(model='cube', position=(pos), scale=(1/SLOWER,1/SLOWER,1/SLOWER),color=color.white)
            il+=1
        else:
            pomel.disable()
        frames = 0
    frames +=1


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
