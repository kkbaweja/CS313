#  File: Blackjack.py
#  Description: A program that plays a game of blackjack
#  Student's Name: Keerat Baweja        
#  Student's UT EID: kkb792
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: 9/22/2016
#  Date Last Modified: 9/23/2016

import random 

# Class that defines deck objects 
class deck:
    all_suit = ["C", "D", "H", "S"]
    all_pip = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cardList = []
        for suit in deck.all_suit:
            for pip in deck.all_pip:
                newCard = card(pip, suit)
                self.cardList.append(newCard)
                 
    def __str__(self):
        counter = 0
        for card in self.cardList: 
            print("", card, end = ',')
            counter += 1
            if counter == 13:
                print("\n", end = ',')
                counter = 0
        return("")

    # Shuffle deck 
    def shuffle(self):
        random.shuffle(self.cardList)

    # Deal one card from deck to each player
    def dealOne(self, player):
        cardToDeal = self.cardList[0]
        player.hand.append(cardToDeal)
        player.handTotal += cardToDeal.value
        self.cardList.pop(0)
    
# Class that defines card objects
class card: 
    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit
        self.value = 0
        if self.pip == "J" or self.pip == "Q" or self.pip == "K":
            self.value = 10
        elif self.pip == "A":
            self.value = 11
        else:
            self.value = int(pip)
            
    def __str__(self):
        description = self.pip + self.suit
        return(description.rjust(3))
    
# Class that defines game player objects
class player:
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def __str__(self):
        for card in self.hand:
            print(" ", card, end = "")
        return("")

# Function to show hands of opponent and dealer at start of game
def showHands(player1, player2):
    print("\nDealer shows", player1.hand[1], "faceup")
    print("You show", player2.hand[1], "faceup")

# Function to allow opponent to take a turn     
def opponentTurn(cardDeck, dealer, opponent):
    dealerGo = True 
    print("\nYou go first.\n")
    # Find out how many aces are in hand 
    str_hand = ""
    for card in opponent.hand:
        str_hand += card.pip + card.suit
    num_aces = str_hand.count("A")
    if num_aces > 0:
        print("Assuming a value of 11 points for all Aces.")

    # Opponent Turn
    if num_aces == 2:
        opponent.handTotal = 2
        
    while opponent.handTotal < 21:
        print("You hold:\n",opponent, "\nCurrent hand total:", opponent.handTotal)
        answer = int(input("1 (hit) or 2 (stay)? "))
        print("")
        if answer == 2:
            print("Staying with", opponent.handTotal)
            return(dealerGo)
        else:
            cardDeck.dealOne(opponent)
            print("Card dealt:", opponent.hand[-1])
            print("New total:", opponent.handTotal)

        # Checking for value of Aces   
        if opponent.handTotal > 21 and num_aces > 0:
            opponent.handTotal -= 10
            num_aces -= 1
            print("\nYou bust. Swtiching the value of one Ace from 11 points to 1 point.")

    # Once opponent has 21 or more points
    if opponent.handTotal == 21:
        print("You have reached 21!")
    else:
        print("You bust. Dealer wins")
        dealerGo = False
    return(dealerGo)

# Function to allow dealer to take a turn
def dealerTurn(cardDeck, dealer, opponent): 
    print("\nDealer's turn.\n")
    print("Your hand:\n", opponent, "\nCurrent total:", opponent.handTotal)

    # Find out how many aces are in hand 
    str_hand = ""
    for card in dealer.hand:
        str_hand += card.pip + card.suit
    num_aces = str_hand.count("A")
    if num_aces > 0:
        print("Assuming a value of 11 points for all Aces.")

    # Dealer turn     
    if num_aces == 2:
        dealer.handTotal = 2
        
    while dealer.handTotal < 21:
        print("Dealer's hand:\n", dealer, "\nCurrent total:", dealer.handTotal)
        cardDeck.dealOne(dealer)
        print("Dealer hits:", dealer.hand[-1])
        print("\nNew total:", dealer.handTotal)

        #Checking for value of Aces
        if dealer.handTotal > 21 and num_aces > 0:
            dealer.handTotal -= 10
            num_aces -= 1
            print("\nDealer busts. Swtiching the value of one Ace from 11 points to 1 point.")

    # Once opponent has 21 or more points
    if dealer.handTotal == 21:
        print("Dealer has reached 21! Dealer wins. You lose.")
    else:
        print("Dealer busts. You win!")
        
        
def main():
    cardDeck = deck()
    print("Initial Deck:")
    print(cardDeck)

    random.seed(50)
    cardDeck.shuffle()
    print("Shuffled Deck")
    print(cardDeck)

    dealer = player()
    opponent = player()

    cardDeck.dealOne(opponent)
    cardDeck.dealOne(dealer)
    cardDeck.dealOne(opponent)
    cardDeck.dealOne(dealer)

    print("Deck after dealing two cards each:")
    print(cardDeck)

    showHands(dealer, opponent)

    dealerGo = opponentTurn(cardDeck, dealer, opponent)
    if dealerGo:
        dealerTurn(cardDeck, dealer, opponent)

    print("\nGame Over.")
    print("Final hands:")
    print("Dealer:\n", dealer)
    print("Opponent:\n", opponent)
    
    

main() 
