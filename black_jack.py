# current working version - - - 02/25/2013

import random
import os

def main():
    print "Welcome To Python Blackjack. [H] Is For A Hit, [S] Is To Stand, [Q] To Quit.\n"
    c = ""    # Hit, Stand or Quit Variable.
    player = deal_cards()   
    dealer = deal_cards()
    print "< ---- Player Hand ---->"
    print "Player Hand: ", player   
    print "Total Player Hand: ", total_hand(player)   
    print
    print "< ---- Dealer Hand ---->"
    print "Dealer Hand: ", dealer                     
    print "Total Dealer Hand: ", total_hand(dealer)
    print
   
    if total_hand(player) == 21:
        print "BLACKJACK! YOU WIN!"
        message()
    else:
        if total_hand(dealer) == 21:
            print "Sorry You Lose! Dealer Wins"
            message()
           
    while c != "q":
        c = raw_input("[H]it [S]tand [Q]uit: ").lower()   
        if c == "h":
            hit(player)        
            print ""
            print "Your Cards Are Now: ",player                
            print "Total For Player Is: ",total_hand(player)
            if total_hand(player) > 21:
                print "BUSTED! Sorry, You Lose."
                message()
            if total_hand(dealer) <= 17: # ? does this needs to be moved so it works whether or not player hits.
                hit(dealer)
                print "\nThe Dealer Takes A Card", dealer
                print "For A Total Of: ", total_hand(dealer)
                if total_hand(dealer) > 21:
                    print "Dealer Busted! You Win!\n"
                    message()
        elif c == "s":
            if total_hand(dealer) <= 17:
                hit(dealer)
                print "The Dealer Takes A Card", dealer
                print "For A Total Of: ", total_hand(dealer)
                if total_hand(dealer) == 21:
                    print "BLACKJACK! Dealer Wins.\n"
                    message()
                elif total_hand(dealer) > 21:
                    print "Dealer Busted! You Win!\n"
                    message()
                elif total_hand(dealer) >= total_hand(player):
                    print "Sorry, You Lose. Dealer Wins\n"
                    message()
                else:
                    total_hand(player) > total_hand(dealer)
                    print "You Win With The Best Hand!\n"
                    message()
            elif total_hand(player) > total_hand(dealer):
                print "You Win With The Best Hand!\n"
                message()
            elif total_hand(dealer) > total_hand(player):
                print "Sorry, You Lose. Dealer Wins"
                message()
        else:
            if c == "q":
                message()
            else:
                print "Invalid Choice. . .To Quit, Press [Q]"
               
               
           
               
               


def deal_cards():
    random1 = random.randint(1,11)
    random2 = random.randint(1,11)
    hand = [random1, random2]
    return hand


def hit(hand):
    newCard = random.randint(1,11)
    hand.append(newCard)
    return hand


def total_hand(hand):
    total = sum(hand)
    return total


def message():
    again = raw_input("Do You Want To Play Again? [Y] For Yes - Press Any Key To Quit: ").lower()
    if "y" in again:
        main()
    else:
        print "Thanks For Playing"
        os._exit(1)


# main

if __name__ == '__main__':
    main()