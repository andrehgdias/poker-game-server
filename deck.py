import random
import constants

class Card:
    def __init__(self, value = -1, suit = "Suit"):
        self.value = value
        self.suit= suit

    def __str__(self):
        return self.value + " of " + self.suit

class Deck:
    values = [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]

    def __init__(self):
        print(f"> [LOG][Deck] Creating a deck\n") if constants.DEBUG else None
        self.cards = [Card(value, suit) for value in self.values for suit in self.suits]

    def reset(self):
        print(f"> [LOG][Deck] Reseting the deck\n") if constants.DEBUG else None
        self.cards = [Card(value, suit) for value in self.values for suit in self.suits]

    def show(self):
        print(f"> [LOG][Deck] Showing all cards in the deck\n") if constants.DEBUG else None
        for card in self.cards:
            print(card)
    
    def shuffle(self):
        print(f"> [LOG][Deck] Shuffling the deck\n") if constants.DEBUG else None
        random.shuffle(self.cards)    

    def draw_card(self):
        print(f"> [LOG][Deck] Drawing a card\n") if constants.DEBUG else None
        return self.cards.pop()

