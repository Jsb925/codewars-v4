from engine.main import Game
import scriptblue
import scriptred
import test1

if __name__ == "__main__":
    G = Game((40, 40), scriptred, test1)
    G.run_game()