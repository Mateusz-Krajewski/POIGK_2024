import os
import sys

sys.path.insert(0, os.path.abspath('./code')) 

from Game import Game

###
SLOWER = 10
###

if __name__ == "__main__":
    Game(SLOWER)