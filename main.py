from game import Game
from exceptions import GameOverCroupierException, GameOverUserException
from player import Player


try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('User wins')
except GameOverUserException:
    print('Croupier win')
