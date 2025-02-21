# this is going to contain the deck class

import random

class Deck:
    def __init__(self,cards):
        self.cards = cards
    
    def getdeck(self):
        return self.cards
    
    def setdeck(self, cards):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)   
    