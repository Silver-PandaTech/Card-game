# this is going to contain the card class

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def getcard(self):
        return f"{self.value} of {self.suit}"
    
    def setcard(self, suit, value):
        self.suit = suit
        self.value = value

    def set_special(self, special):
        self.special = special

    def get_special(self):
        return self.special
