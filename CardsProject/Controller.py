import ConsoleView as gr
import PlayerClasses.PlayerClasses as pc
import CardClasses.CardsClub as cc


class Controller:
    def __init__(self):
        self.displayPort = gr.graphics()
        self.playerTerminal = gr.playerTerminal()
        ##deckSize 52 per default
        self.cardSizeMultiplier = 1
        self.playedRounds = 0

    def startSession(self):
        #example of playingCard object creation in a list
        displayHand = [cc.playingCard(0,1,12,"Spades"),cc.playingCard(0,1,11,"Spades"),cc.playingCard(0,1,0,"Spades")]
        self.displayPort.welcomeMessage(displayHand)
        playerMenuInput = int(self.playerTerminal.requestMenu())

        match playerMenuInput:
            case 1:
                self.startGame()
            case 2:
                self.editDeck()
            case 3:
                self.startSession()
                
   
    def editDeck(self):
        self.cardSizeMultiplier = self.playerTerminal.askDeckMultiple()
        self.startSession()
    
    def playerInitiation(self):
        playerAmount = self.playerTerminal.playerAmount()
        playerList = []
        for i in range(playerAmount):
           playerName = self.playerTerminal.playerName(i+1)
           beginningBalance = self.playerTerminal.playerBeginningBalance(playerName)
           ##declaring player and dealer objects
           player = pc.competitivePlayer(beginningBalance,playerName)
           playerList.append(player)
        return playerList
        
    def startGame(self):
       dealer = pc.Dealer()
       playerList = self.playerInitiation()
       ##Creating deck card object; multiplier to size of deck value; generating the deck with deckLength and shuffling of the deck
       deck = cc.deckOfCards()
       deckSize = deck.deckSizeMultiplier(self.cardSizeMultiplier)
       deck.generateDeck()
       deck.shuffle()
       flag = 'idle'
       while (flag != ''):
           flag = self.playerTerminal.beginningGameInfoDisplay(deckSize)
       self.gameLoop(deck,playerList,dealer)

    #function when declared will call upon the player class method to return a player hand value.
    def playerHandValue(self,player):
        playerHand = player.handValueCalculation()
        return playerHand

    def playerBet(self,player):
        flagHold = True
        while flagHold:
           totalBet = self.playerTerminal.roundBet(player.playerName)
           #player.placeBet() returns a True or False whether the bet is valid; if valid the bet will be withdrawn from the player's balance
           result = player.placeBet(totalBet)
           #display message depending on result of result
           self.displayPort.ifBetValid(result,totalBet)
           #flagHold is the negation of result
           flagHold = not result
        return totalBet

    #arguments are as follows:
    #deck: deck of cards object
    #playerList: list of player object
    #dealer: dealer player Object
    def gameLoop(self,deck,playerList,dealer):
       #2 is the number of cards dealt per individual at the start
       self.playedRounds += 1
       self.displayPort.perRoundInfo(self.playedRounds,playerList)
       activeBets = [(self.playerBet(o) == 0) for o in playerList]
       filtered_List = [i for (i,v) in zip(playerList,activeBets) if not v]
       if all(activeBets):
           self.closeGame()
       else:
           pass
       playerList = filtered_List
       totalPlayers = len(playerList)   
       self.beginRoundDealing(deck,playerList,dealer,2,totalPlayers)

         
    def beginRoundDealing(self,deck,playerList,dealer,cardsPerPlayer,totalPlayers):
        #For loop at the beginning of the round to dealCards
        for i in range(cardsPerPlayer):
            for p in range(totalPlayers):
                currentPlayer = playerList[p]
                playerDealtCard = deck.drawCard()
                playerDealtCard.flipFace(1)
                currentPlayer.hitToHand(playerDealtCard)
                self.displayPort.playerHandDisplay(currentPlayer.playerName,currentPlayer.playerHand)
            dealerDealtCard = deck.drawCard()
            if (i == 0):
                dealerDealtCard.flipFace(1)
            else:
                dealerDealtCard.flipFace(0)
            dealer.hitToHand(dealerDealtCard)
            self.displayPort.playerHandDisplay("Dealer",dealer.playerHand)

        #initialising a list keeping track of players in multiPlayerChannel
        playersInPlay = [False] * totalPlayers
        for i in range(totalPlayers):
            naturalBlackJackCheck = self.valueCheck(playerList[i])
            playersInPlay[i] = naturalBlackJackCheck
            if (naturalBlackJackCheck):
                self.displayPort.naturalBlackJack(playerList[i].playerName)
        self.multiPlayerChannel(deck,dealer,playerList,playersInPlay,totalPlayers,0)


    def valueCheck(self,player):
        valueCheck = self.playerHandValue(player)
        playerBet = player.currentRoundBet
        if (valueCheck == 21):
            return True
        elif (valueCheck > 21):
            self.displayPort.bust(valueCheck,player.playerName)
            return True
        else:
            return False

    
    def multiPlayerChannel(self,deck,dealer,playerList,playersInPlay,totalPlayers,accumalatedPlayerTotal):
        if (accumalatedPlayerTotal > (totalPlayers-1)):
            firstRoundBoolean = False
        else:
            firstRoundBoolean = True
       #create scenerio for all blackjacks
        if all(playersInPlay):
            self.displayPort.roundFinished()
            self.dealerPlay(deck,dealer,playerList,totalPlayers)
            self.endRoundClear(deck,playerList,totalPlayers,dealer)
        else:
            currentPlayerIndex = accumalatedPlayerTotal % (totalPlayers)
            #playerInRound is the disjunction of two boolean variables; whether the player's round has already ended and second
            #a boolean variable determined by the value of a given player's hand
            playersInPlay[currentPlayerIndex] = playersInPlay[currentPlayerIndex] or self.valueCheck(playerList[currentPlayerIndex])
            #Upon establishing if the player is still in play; the player can commence their round
            #horrible implementation needs change
            if (playersInPlay[currentPlayerIndex] == False):
                player = playerList[currentPlayerIndex]
                result = self.roundLoop(deck,player,dealer,firstRoundBoolean)
                if (type(result) == bool):
                    playersInPlay[currentPlayerIndex] = result
                else:
                    playerList.insert((currentPlayerIndex+1),result)
                    playersInPlay.insert((currentPlayerIndex+1),False)
                    playersInPlay[currentPlayerIndex] = False
                    totalPlayers += 1
                    accumulatedPlayerTotal += 1
            else:
                pass
            nextPlayerAdd = accumalatedPlayerTotal + 1
            self.multiPlayerChannel(deck,dealer,playerList,playersInPlay,totalPlayers,nextPlayerAdd)
        
    def roundLoop(self,deck,player,dealer,firstRoundBoolean):
        ##implement beginning round bet
        self.displayPort.playerTurn(player.playerName)
        self.displayPort.displayGivenHand(player.playerHand)
        handValueCards = [o.value for o in player.playerHand]
        splitTrue = checkList(handValueCards)
        #second argument is to determine if the player can split
        playAction = self.playerTerminal.playerPlayChoices(firstRoundBoolean,splitTrue)
        match playAction:
            case 1:
                #turn into function
                playerDealtCard = deck.drawCard()
                playerDealtCard.flipFace(1)
                player.hitToHand(playerDealtCard)
                self.displayPort.playerHandDisplay(player.playerName,player.playerHand)
                return self.valueCheck(player)
            case 2:
                return True
            case 3:
                #For the bet to be doubled player must add the same amount to their bet doubling the total
                #system will also validate if player has the possible balance to make this double
                #failure to do so will open up player actions again (input system to remove this opinion without player possibly an enumerated for loop with possible options)
                if (firstRoundBoolean):
                    self.displayPort.playerDoubleDown(player.playerName)
                    playerBet = player.currentRoundBet
                    result = player.placeBet(playerBet)
                    doubleBet = 2 * playerBet
                    if (result):
                        self.displayPort.ifBetValid(result,doubleBet)
                        player.currentRoundBet = doubleBet
                        return False
                    else:
                        self.displayPort.ifBetValid(result,doubleBet)
                        self.roundLoop(deck,player,dealer,False)
                else:
                    self.displayPort.invalidOption()
                    self.roundLoop(deck,player,dealer,False)
            case 4:
                if (firstRoundBoolean):
                    self.displayPort.surrenderHand(player.playerName)
                    player.handValue = -1
                    return True
                else:
                    self.displayPort.invalidOption()
                    self.roundLoop(deck,player,dealer,False)
            case 5:
                #Split functionality is currently unoperational
                if (firstRoundBoolean and splitTrue):
                    #creates a new instance of a player attributed as the split hand
                    masterName = player.playerName
                    cardHit = player.drawCardFromHand()
                    givenBet = player.currentRoundBet
                    splitPlayer = pc.split(masterName,cardHit,givenBet)
                    return splitPlayer
                else:
                    self.displayPort.invalidOption()
                    self.roundLoop(deck,player,dealer,False)
                    
                    
    def endRoundClear(self,deck,playerList,totalPlayers,dealer):
        for i in range(totalPlayers):
            currentPlayer = playerList[i]
            playerHand = currentPlayer.playerHand
            ##A list comprehension ensuring all cards returning to the deck are face down
            formattedHand = [playerHand[i].flipFace(0) for i in range(len(playerHand))]
            deck.returnCards(playerHand)
            currentPlayer.clearHand()
        dealerHand = dealer.playerHand
        formattedHand = [dealerHand[i].flipFace(0) for i in range(len(dealerHand))]
        deck.returnCards(dealerHand)
        dealer.clearHand()
        self.gameLoop(deck,playerList,dealer)
        pass
        
    def bustPath(self,player):
        self.displayPort.bust(player.handValueCalculation(),player.playerName)
        self.displayPort.bust(player.handValueCalculation())
        pass
    def winPath(self,player,playerBet):
        #self.displayPort.blackJackWin()
        betGain = playerBet * 1.5
        self.displayPort.betGain(player.playerName,betGain)
        player.winBet(betGain)
        pass
    def compareHands(self,dealerHandValue,playerList,totalPlayers):
        for i in range(totalPlayers):
            currentPlayer = playerList[i]
            playerName = currentPlayer.playerName
            playerBet = currentPlayer.currentRoundBet
            playerHandValue = currentPlayer.handValueCalculation()
            if ((dealerHandValue > playerHandValue) and (dealerHandValue <= 21) and (playerHandValue <= 21) and (playerHandValue > 0)):
                self.displayPort.beatenByDealer(playerName)
            elif(playerHandValue == -1):
                playerHalfBet = playerBet/2
                currentPlayer.winBet(playerHalfBet)
                #player has surrendered
                pass
            elif ((playerHandValue > 0) and (dealerHandValue == 22) and (playerHandValue < 29) and (playerHandValue > 21)):
                self.displayPort.pushTwentyTwo(playerName)
                currentPlayer.winBet(playerBet)
            elif(playerHandValue > 21):
                self.displayPort.userBustLose(playerName)
            elif ((dealerHandValue == playerHandValue) and (playerHandValue <= 21)):
                self.displayPort.userDraw(playerName)
                currentPlayer.winBet(playerBet)
            elif ((playerHandValue > dealerHandValue) and (playerHandValue <= 21)):
                self.displayPort.userWin(playerName)
                self.winPath(currentPlayer,playerBet)
            elif (playerHandValue == 21):
                self.displayPort.nonNaturalBlackJack(playerName)
                self.winPath(currentPlayer,playerBet)
            else:
                self.winPath(currentPlayer,playerBet)
                self.displayPort.userWin(playerName)
        pass
    def dealerPlay(self,deck,dealer,playerList,totalPlayers):
        dealerHand = dealer.playerHand
        shownHand = [dealerHand[i].flipFace(1) for i in range(len(dealerHand))]
        self.displayPort.dealerShowsHand(dealerHand)
        dealerHandValue = self.playerHandValue(dealer)
        if dealerHandValue > 17:
            self.displayPort.dealerStick()
            self.compareHands(dealerHandValue,playerList,totalPlayers)
            pass
        else:
            while (dealerHandValue < 17):
                if(dealerHandValue == 21):
                    self.displayPort.blackJackWin()
                elif(dealerHandValue > 21):
                    self.displayPort.dealerBust()
                else:
                    dealerDealtCard = deck.drawCard()
                    dealerDealtCard.flipFace(1)
                    dealer.hitToHand(dealerDealtCard)
                    self.displayPort.playerHandDisplay("Dealer",dealer.playerHand)
                    dealerHandValue = self.playerHandValue(dealer)
            self.displayPort.displayComparehands()
            self.compareHands(dealerHandValue,playerList,totalPlayers)
        pass
    
    def closeGame(self):
        self.displayPort.endGame()
        quit()

##helper functions:

def checkList(lst):
    ele = lst[0]
    chk = True
    for item in lst:
        #checks cards that are not face cards or 10s whether they are identical
        #Side note: values begin at 0; hence a 10 card will be valued 9
        if (ele != item) and ((item < 9) or (ele < 9)):
            chk = False
            break
    return chk

