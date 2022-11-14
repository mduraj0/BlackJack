from game import Game
from exceptions import GameOverCroupierException, GameOverUserException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('User wins')
except GameOverUserException:
    print('Croupier win')

