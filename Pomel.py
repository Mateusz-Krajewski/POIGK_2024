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