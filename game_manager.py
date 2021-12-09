from random import choice
from typing import Tuple
from deck import Deck
from utils import GameState, Action
from game import Game, Player
import constants
       
class GameManager:
    def __init__(self):
        self.game = Game()
    
    def create_game(self, p1, p2):
        ("> [LOG][GameManager] Creating game\n") if constants.DEBUG else None

        # Setting up the game and the players
        self.game = Game(p1, p2)

        # Creating game deck
        self.deck = Deck()

    def describe(self):
        print(f"> [LOG][GameManager] Describing current game\n") if constants.DEBUG else None
        print(self.game)
 
    def handle_game(self, game) -> Player:
        small_blind, big_blind = game.small_blind, game.big_blind
            
        if game.state == GameState.PRE_FLOP:
            print(f"\n================================================================================\n")
            print(f"> [LOG][GameManager] Current level: {self.game.current_level}\n") if constants.DEBUG else None
            print(f"> [LOG][GameManager] Small blind value: {self.game.sb_value} chips\n") if constants.DEBUG else None
            print(f"> [LOG][GameManager] Starting pre-flop\n") if constants.DEBUG else None

            game.add_to_pot(small_blind.remove_chips(game.sb_value)) # Adding small blind to pot
            game.add_to_pot(big_blind.remove_chips(game.sb_value * 2)) # Adding big blind to pot
            
            # First Betting Round: SB start Bet pre-flop -> start betting logic
            small_blind_action = small_blind.act(game)
            big_blind_action = None

            if small_blind_action == Action.FOLD:
                return big_blind

            elif small_blind_action == Action.CHECK:
                big_blind_action = big_blind.act(game)
                game.state = GameState.FLOP
                self.handle_game(game)

            else:
                print("Small Betou")

            # This return is temporary
            return small_blind

        if game.state == GameState.FLOP:
            print(f"> [LOG][GameManager] Starting flop\n") if constants.DEBUG else None
        # Burn and Show 3 cards at flop
        # Second Betting Round: BB start Bet pos-flop -> start betting logic
        
        if game.state == GameState.TURN:
            print(f"> [LOG][GameManager] Starting turn\n") if constants.DEBUG else None
        # Burn and Show 1 card at turn
        # Third Betting Round: BB start Bet pos-turn -> start betting logic
        
        if game.state == GameState.RIVER:
            print(f"> [LOG][GameManager] Starting river\n") if constants.DEBUG else None
        # Burn and Show 1 card at river
        # Fourth Betting Round: BB start Bet pos-river -> start betting logic
        
        # Showdown
        # BB than SB
        
        return small_blind

    def start_game(self):
        print(f"> [LOG][GameManager] Starting game\n") if constants.DEBUG else None
        print(f"> [LOG][GameManager] Assign Button and Small Blind\n") if constants.DEBUG else None
        self.game.small_blind = self.game.button = choice([self.game.p1, self.game.p2]) 

        print(f"> [LOG][GameManager] Assign Big Blind\n") if constants.DEBUG else None
        self.game.big_blind = (self.game.p2 if self.game.button == self.game.p1 else self.game.p1)

        print(f"> [LOG][GameManager] SB and Button: {self.game.button}\n") if constants.DEBUG else None
        print(f"> [LOG][GameManager] BB: {self.game.big_blind}\n") if constants.DEBUG else None
        
        quit = False

        while not quit:
            self.deck.shuffle()

            print(f"> [LOG][GameManager] Dealing hands\n") if constants.DEBUG else None
            self.game.big_blind.hand = (self.deck.draw_card(), self.deck.draw_card())
            self.game.small_blind.hand = (self.deck.draw_card(), self.deck.draw_card())
        
            print(f"> [LOG][GameManager] P1({self.game.p1.name})'s hand: {self.game.p1.show_hand()}\n") if constants.DEBUG else None
            print(f"> [LOG][GameManager] P2({self.game.p2.name})'s hand: {self.game.p2.show_hand()}\n") if constants.DEBUG else None
            
            print(self.game)
            hand_winner = self.handle_game(self.game)
            hand_winner.add_chips(self.game.pot)
            print(f"{hand_winner}, wins {self.game.pot} chips with a {hand_winner.show_hand()}!")
            
            quit = True if input("\nQuit game(y/n)? \n") == 'y' else False
            if not quit:
                self.game.reset()
                self.deck.reset()


