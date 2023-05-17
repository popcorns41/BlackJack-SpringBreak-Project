#Algorithm to produce a deck of card objects 
#Suit symbol icons has been removed in this version

Red, Black = True, False

class playingCard:
    ## expected values for each class attribute
    ## colour = Red(True),Black(False)
    ## reveal = True (show face of card), False(show back of card)
    ## value = integer value from 0 to 13 (special cases: 0 - ace; 11 - Jack; 12 - Queen; 13-King
    ## suit = string value from 4 options: Clubs, Diamonds, Hearts, and Spades

    def __init__(self,colour,displaySide,value,suit):
        self.colour = colour
        self.reveal = displaySide
        self.value = value
        self.suit = suit
    def flipFace(self,reveal):
        self.reveal = reveal


def generateDeck(deckSizeMultiplier = 1):
    L = 52 * deckSizeMultiplier
    quarter = int(L/4)
    half = int(L/2)
    suits = ["Clubs","Diamonds","Hearts","Spades"]
    cardDeck = []
    for i in range(0,L):
        value = i % quarter
        suitValue = int(i/quarter)
        colour = Black if (half < i) else Red
        cardDeck.append(playingCard(colour,False,value,suits[suitValue]))
    return cardDeck