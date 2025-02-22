# this is going to contain the card class
import random


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
    
    def getvalue(self):
        return self.value
    
    def setvalue(self,value):
        self.value = value
    



    
def draw_card(deck):
    card = deck.pop()
    return card
    


def is_odd(num):
    if (num % 2) != 0:
        return True
    else:
        return False



def create_deck(suits,values,special):
    deck = []
    for suit in suits:
        for value in values:
            card = Card(suit, value)
            random_int = random.randint(1,10)
            if is_odd(random_int) is True:
                if random_int < 6:
                    card.set_special(special[1])
                else:
                    card.set_special(special[0])
            else:
                card.set_special(special[2])
            
            deck.append(card)
    random.shuffle(deck)
    return deck

