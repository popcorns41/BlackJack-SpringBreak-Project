#redefined hiearchy player, dealer compeitivePlayer


#remove constructor for gone bust can control it in the multiplayer controller
class Player:
    def __init__(self):
        self.playerHand = []
        self.handValue = 0
        self.aceQuantity = 0
    def hitToHand(self,card):
        cardValue = card.value
        ##if statement attributing different card values respective to playingCard
        ##objects (due to indexing of card values face values are one less than blackjack value by 1
        if (1 <= cardValue <= 9):
            self.handValue += (cardValue + 1)
        elif(cardValue > 9):
            self.handValue += 10
        elif (cardValue == 0):
            self.aceQuantity += 1
        self.playerHand.append(card)
    #implement ace calculation improve after viewing coin question xx
    def recursionAceCalculation(self,value):
        if (value <= 21):
            return value
        else:
            #recursively goes through aces to find optimal ones and 11s in your hand
            # minus 10 is the value after subtracting 10 and adding 1 to the value
            return self.recursionAceCalculation(value-10)
        
    def handValueCalculation(self):
        #Filtering special case where no matter the arrangement of aces; hand is still a bust
        if (self.handValue != -1):
            lowCase = self.handValue + (self.aceQuantity)
            if (lowCase > 21):
                return lowCase
            elif (self.aceQuantity == 0):
                return self.handValue
            else:
                #initial highCase is the value of your other cards (handValue) + the number of aces * 11
                #this process is done recursively
                highCase = self.handValue + (self.aceQuantity * 11)
                highCaseCal = self.recursionAceCalculation(highCase)
                return highCaseCal
        else:
            return self.handValue
    def clearHand(self):
        self.playerHand = []
        self.handValue = 0
        self.aceQuantity = 0
    #returns a card from a given index of the hand; the function by default will pick the first card of the hand
    def drawCardFromHand(self,index = 0):
        return self.playerHand.pop(index)
        

    #bust is boolean true or false

class competitivePlayer(Player):
    def __init__(self,totalBettingCash,playerName):
        super().__init__()
        self.playerBank = totalBettingCash
        self.playerName = playerName
        self.currentRoundBet = 0
        self.splitBool = False
        #For split hands; 0 meaning not in use; 1 meaning only first hand; 2 meaning only second hand; 3 meaning both hands in play 
        self.cardInPlayDeclare = 0
        self.splitPlayer = None
    def placeBet(self,betAmount):
        if ((self.playerBank - betAmount) < 0):
            return False
        else:
            ##Total betting cash avaliable will be displayed in control
            self.playerBank -= betAmount
            self.currentRoundBet = betAmount
            return True
    #called when a player calls split; an empty hand in the player class will be filled with the first card of their hand and will be treated as a secondary player
    def initiateSplit(self):
        self.splitBool = True
        masterName = self.playerName
        cardHit = self.drawCardFromHand()
        givenBet = self.currentRoundBet
        self.splitPlayer = split(masterName,cardHit,givenBet)
        
    def winBet(self,betGain):
        self.playerBank += betGain

class split(Player):
    def __init__(self,masterName,dealtsplitHand,givenBet):
        super().__init__()
        self.playerName = "player " + str(masterName) + ".2"
        self.playerHand = [dealtsplitHand]
        self.currentRoundBet = givenBet
        

class Dealer(Player):
    pass
