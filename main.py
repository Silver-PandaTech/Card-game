#Silver-pandatech
#This is a simple program to play a game of make belive cards.
# I have no idea where this is going, so take it as it is.
# I'm just getting some practice in with python

import cards
import random

def is_odd(num):
    match num:
        case 1 | 3 | 5 | 7 | 9:
            return True
        case _:
            return False

def main():
    #this will set the suits we can use->
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    #this will set the values we can use->
    values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    #this will set the special values we can use->
    special = ["Dark", "Light", "None"]

    #we need to create the cards now that we have the suits and values and specials
    deck = []
    for suit in suits:
        for value in values:
            card = cards.Card(suit, value)
            random_int = random.randint(1,10)
            if is_odd(random_int) is True:
                if random_int < 6:
                    card.set_special(special[1])
                else:
                    card.set_special(special[0])
            else:
                card.set_special(special[2])
            
            deck.append(card)

    for cards1 in deck:
        print(cards1.getcard())
        if cards1.get_special() != "None":
           print(cards1.get_special())
        print("_______________________")
        
        
            

main()

