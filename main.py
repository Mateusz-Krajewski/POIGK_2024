from Generator import Generator
from Game import Game

###
SLOWER = 10
###

if __name__ == "__main__":
    generator = Generator(SLOWER)
    do = generator.GenerateSphere(1,60,80)
    game = Game(do, SLOWER)