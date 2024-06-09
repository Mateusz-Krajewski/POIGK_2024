from Generator import Generator
from Game import Game

###
SLOWER = 10
###


generator = Generator(SLOWER)


do = generator.GenerateSphere(1,60,80)
game = Game(do, SLOWER)