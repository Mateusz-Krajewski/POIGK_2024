import os
import sys

sys.path.insert(0, os.path.abspath('./code'))

from Game import Game  # pylint: disable=all

###
SLOWER = 10
###

if __name__ == "__main__":
    """
    Główna funkcja uruchamiająca grę.
    Importuje wymagane moduły, dodaje ścieżkę do kodu gry, 
    importuje klasę Game z modułu Game i uruchamia grę 
    z podanymi parametrami.
    """
    Game(SLOWER, 1.15, 2)
