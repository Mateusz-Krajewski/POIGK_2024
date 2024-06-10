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

    Konfiguracja:
    SLOWER: int - Zmienna określająca prędkość gry.

    Uruchomienie:
    Game(SLOWER, 1.15, 2)
    - Pierwszy parametr: prędkość gry (int)
    - Drugi parametr: ilość warstr w pionie (float)
    - Trzeci parametr: ilość punktów w poziomej warstwie (int)
    """
    Game(SLOWER, 1.15, 2)
