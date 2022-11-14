from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print('Press 1 to take card')
        print('Press 2 to pass')

    def _croupier_plays(self, user_points):
        croupier = Player()
        while croupier.calculate_points() < user_points:
            croupier.take_card(self.deck.hit_card())
            print('Croupier cards:')
            print(croupier.cards)
            print(croupier.calculate_points())

        return croupier.calculate_points()

    def _user_plays(self):
        user = Player()
        for _ in range(2):
            card = self.deck.hit_card()
            user.take_card(card)

        while True:
            print(user.cards)
            print(user.calculate_points())
            self._print_menu()
            choice = input()
            if choice == '1':
                user.take_card(self.deck.hit_card())

            elif choice == '2':
                return user.calculate_points()

            else:
                print('Bad choice!')

    def play(self):
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error

        try:
            croupier_points = self._croupier_plays(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error
        print(f'Croupier points {croupier_points}, User points {user_points}')
        print('The end, croupier win!')

