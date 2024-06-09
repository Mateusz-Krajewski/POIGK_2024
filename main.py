import os
import sys

sys.path.insert(0, os.path.abspath('./code')) 

from Game import Game

###
SLOWER = 10
###


class Main:
    def __init__(self) -> None:
        game = Game(SLOWER)


if __name__ == "__main__":
    Main()