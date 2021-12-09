from deck import Card
from utils import Action, GameState
import constants

class Player:
    def __init__(self, name = "Dummy", hand = (Card(), Card()), stack = 0):
        self.name = name
        self.hand = hand
        self.stack = stack

    def __str__(self):
        return f"{self.name} with {self.stack} chips in total"

    def add_chips(self, chips):
        self.stack += chips
        return chips

    def remove_chips(self, chips):
        self.stack -= chips
        return chips

    def show_hand(self):
        return f"{self.hand[0]} / {self.hand[1]}"
    
    def handle_action(self):
        print('''
Choose your action:
1. Fold
2. Check
3. Bet
            ''')
        option = input("Opção: ")
        if option == '1':
            print(f"> [LOG][Player] {self.name} Folded\n") if constants.DEBUG else None
            return Action.FOLD
        if option == '2':
            print(f"> [LOG][Player] {self.name} Checked\n") if constants.DEBUG else None
            return Action.CHECK
        if option == '3':
            print(f"> [LOG][Player] {self.name} Bet\n") if constants.DEBUG else None
            return Action.BET

    def act(self, game):
        print(self)
        print(self.show_hand())
        print(f"Current pot: {game.pot}")
        print(f"Public cards: {game.show_board()}")
        return self.handle_action()

class Game:
    def __init__(self, p1 = Player(), p2 = Player(), initial_stack = 10000, initial_bb = 100, levels = 6, level_duration = 15, current_level = 1):
        self.p1 = p1
        self.p2 = p2

        if p1.stack == 0:   
            self.p1.stack = initial_stack
            self.p2.stack = initial_stack
        
        # Game configuration
        self.initial_stack = initial_stack
        self.initial_bb = initial_bb
        self.levels = levels
        self.level_duration = level_duration
        self.state = GameState.PRE_FLOP
        self.public_cards = ()
        self.pot = 0
        self.current_level = current_level
        self.sb_value = initial_bb/2
            
        # Positions
        self.button = None
        self.small_blind = Player()
        self.big_blind = Player()

    def __str__(self):
        return (f"Player 01: {self.p1}\n" +
                f"Player 02: {self.p2}\n" +
                f"SM and Button: {self.button}\n" +
                f"BB: {self.big_blind}\n" +
                f"Initial stack: {self.initial_stack}\n" +
                f"Initial Big Blind: {self.initial_bb}\n" +
                f"Numer of levels: {self.levels}\n" +
                f"Current level: {self.current_level}\n" +
                f"Current pot: {self.pot}\n" +
                f"Level duration(minutes): {self.level_duration}\n")
    
    def reset(self):
        print(f"> [LOG][Deck] Reseting the game\n") if constants.DEBUG else None
        old_small_blind = self.small_blind
        old_big_blind = self.big_blind
        current_level = self.current_level

        self.__init__(self.p1, self.p2, self.initial_stack, self.initial_bb, self.levels, self.level_duration)
        # new_game = Game(self.p1, self.p2, self.initial_stack, self.initial_bb, self.levels, self.level_duration)
        self.small_blind = self.button = old_big_blind
        self.big_blind = old_small_blind

        if current_level > 1:
            self.sb_value = self.initial_bb * self.current_level if self.current_level < 6 else self.initial_bb * 10

    def add_to_pot(self, chips):
        self.pot += chips

    def show_board(self):
        for card in self.public_cards:
            print(card)
 
