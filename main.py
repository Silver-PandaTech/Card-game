#Silver-pandatech
#This is a simple program to play a game of make belive cards.
# I have no idea where this is going, so take it as it is.
# I'm just getting some practice in with python

import cards


def main():
    #this will set the suits we can use->
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    #this will set the values we can use->
    values = [2,3,4,5,6,7,8, 9,10,"J","Q","K","A"]
    #this will set the special values we can use->
    special = ["Dark", "Light", "None"]

    #we need to create the cards now that we have the suits and values and specials
    your_deck = cards.create_deck(suits,values,special)
    my_deck = cards.create_deck(suits,values,special)

    #for cards1 in deck:
     #   print(cards1.getcard())
      #  if cards1.get_special() != "None":
      #     print(cards1.get_special())
       # print("_______________________")

    your_score = 0
    my_score = 0

    while True:
        your_card = cards.draw_card(your_deck)
        my_card = cards.draw_card(my_deck)
        print("Your card is " + your_card.getcard() + ", Special attribute: " + your_card.get_special())
        print("My card is " + my_card.getcard() + ", Special attribute: " + my_card.get_special())

        #if your_card.getvalue() == 'J' or 'K' or 'Q' or 'A':
         #   your_card.setvalue(10)

        match (your_card.getvalue()):
            case "J":
                your_card.setvalue(10)
            case "Q":
                your_card.setvalue(10)
            case "K":
                your_card.setvalue(10)
            case "A":
                your_card.setvalue(10)
        your_score += your_card.getvalue()
        
        match (my_card.getvalue()):
            case "J":
                my_card.setvalue(10)
            case "Q":
                my_card.setvalue(10)
            case "K":
                my_card.setvalue(10)
            case "A":
                my_card.setvalue(10)
        my_score += my_card.getvalue()

        print(your_score)
        print(my_score)
        
        if your_score == 21:
            print('You won!!!!!!! Sorry me')
            break
        if my_score == 21:
            print('I won!!! Sorry you')
            break
        if your_score > 21:
            print('You Lost!!! Grats me!!')
            break
        if my_score > 21:
            print('I lost!! Good on you!!')
            break

    print(len(my_deck))
    print(len(your_deck))

            

main()

