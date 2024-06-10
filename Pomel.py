import os
import sys
sys.path.insert(0, os.path.abspath('./code')) 

from Move import Move
from ursina import color, Entity

class Pomel(Entity):
    """
    The Pomel class is responsible for moving the Pomel model and generating the printing effect.

    Args:
        do (list[Move]): List of moves.
        slower (int): Parameter to change print resolution.
    """
    def __init__(self,do:list[Move],slower, **kwargs):
        """
        Initialize the Pomel with a list of moves and a print resolution parameter.

        Args:
            do (list[Move]): List of moves.
            slower (int): Parameter to change print resolution.
        """
        self.frames = 0
        self.do = do
        self.il = 0
        self.speedDivision = 2
        self.slower = slower
        self.pause = False
        self.entitis: list[Entity] = []
        super().__init__(model='cube', position=(0.5, 1.15,0.5),
                                    scale=(.1,.1,.1), origin_z=0, color=color.red, on_cooldown=False)
    
    def ChangePause(self):
        """
        Toggle the pause state.
        """
        self.pause = not self.pause

    def dropEntity(self):
        """
        Delete printed items.
        """
        for e in self.entitis:
            e.disable()
    def enableEntity(self):
        """
        Enable printed items.
        """
        for e in self.entitis:
            e.enable()

    def update(self):
        """
        Function called by the Ursina engine to update the position of the Pomel.
        """
        if not self.pause:
            if self.frames > self.speedDivision:
                if len(self.do) > self.il:
                    self.set_position(self.do[self.il].get_position())
                    if not self.do[self.il].only_move:
                        pos = self.position
                        pos[0] += 0
                        pos[1] -= 0.1
                        pos[2] += 0
                        self.entitis.append(Entity(model='cube', position=(pos), scale=(1/self.slower,1/self.slower,1/self.slower),color=color.black))
                    self.il+=1
                else:
                    self.disable()
                self.frames=0
            self.frames+=1