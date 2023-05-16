import random
import CardClasses.cardGenerationMethods as cgm

Red, Black = True, False

class playingCard:
    ## expected values for each class attribute
    ## colour = Red(True),Black(False)
    ## reveal = True (show face of card), False(show back of card)
    ## value = integer value from 0 to 13 (special cases: 0 - ace; 11 - Jack; 12 - Queen; 13-King
    ## suit = string value from 4 options: Clubs, Diamonds, Hearts, and Spades
    ##Little note: There is no sanitation for these attributes so please follow the format thank you :)

    def __init__(self,colour,displaySide,value,suit):
        self.colour = colour
        self.reveal = displaySide
        self.value = value
        self.suit = suit
        self.suitSymbol = cgm.suitSymbol(suit)
    def flipFace(self,reveal):
        self.reveal = reveal
        
class deckOfCards:
    def __init__(self):
        self.cardDeck = []
        self.deckSize = 52
    def generateDeck(self):
        L =self.deckSize 
        quarter = int(L/4)
        half = int(L/2)
        suits = ["Clubs","Diamonds","Hearts","Spades"]
        for i in range(0,L):
            value = i % quarter
            suitValue = int(i/quarter)
            self.cardDeck.append(playingCard(Black,False,value,suits[suitValue]))
    def deckReset(self):
        self.cardDeck = []
    def deckSizeMultiplier(self,m):
        return self.deckSize * m
    def shuffle(self):
        random.shuffle(self.cardDeck);
    def drawCard(self):
        drawnCard = self.cardDeck.pop()
        #update deck length after pop
        self.deckLength = len(self.cardDeck)
        return drawnCard
    ##playingCard variable is a playingCard object
    def returnCards(self,playingCard):
        #error change
        self.cardDeck= playingCard + self.cardDeck
        #update deck length after push
        self.deckLength = len(self.cardDeck)

    
