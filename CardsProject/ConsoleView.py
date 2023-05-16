import CardClasses.cardGenerationMethods as cgm
import CardClasses.GraphicsMethods as cvm



#display messages

##Inputs from player        
class playerTerminal:
        def playerAmount(self):
                print("\n-------- PLAYERS --------")
                return int(input("Input total number of players: "))
        def playerName(self,playerNumber):
                print("\n----- PLAYER "+ str(playerNumber) + " NAME ------")
                return str(input("Player " + str(playerNumber) + " please input your player name: "))
        def requestMenu(self):
                print("\n-------- MENU --------")
                print("1.play")
                print("2.Change deck size")
                print("3.Exit")
                return int(input("Select an option and confirm with enter: "))
        def playerBeginningBalance(self,playerName):
                print("\n------ BALANCE -------")
                print("Player",playerName,"please input an amount for your betting balance")
                print("pay out is 3 to 2 odds")
                print("surrender yields half of your bet returned")
                return int(input("\nEnter amount (£): "))
        def beginningGameInfoDisplay(self,deckSize):
                print("\n----- INITIALIZE ------")
                print("Deck has been shuffled via the Python Library 'Random'")
                print("Deck size is: ",deckSize,"\n")
                return str(input("Ready to play? (press enter): "))
        def askDeckMultiple(self):
                print("\nThis game by default sets the deck to 52 playing cards")
                return int(input("Please input an integer to multiply the deck by:"))
        ##Mid-gameplay inputs
        def playerPlayChoices(self,showFirstRound,showSplit = False):
                print("\n------- PLAYER -------")
                print("1.Hit")
                print("2.Stick")
                if (showFirstRound):
                        print("3.Double-Down")
                        print("4.Surrender")
                        if (showSplit):
                                print("5.Split hand")
                return int(input("Select an option and confirm with enter: "))
        def roundBet(self,playerName):
                print("\n----- PLAYER BET -----")
                return float(input(str(playerName) + " place your bet at the beginning of the round: (enter 0 to exit the game)"))

#FrontEnd graphics and messages
class graphics:
        ##Ascii representation of cards
        def displayGivenHand(self,hand):
                print(cvm.ascii_version_of_card(hand))
                pass
        def playerHandDisplay(self,playerName,playerHand):
                print("\n--------------")
                print("Player:",playerName,"has been dealt a card")
                self.displayGivenHand(playerHand)
                pass
        ##Displaying player content
        def welcomeMessage(self,displayCards):
                self.displayGivenHand(displayCards)
                print("   Welcome to Python BlackJack!\n")
                pass
        def displayPlayerHandValue(self,handValue):
                print("Player hand score is:",handValue)
                pass
        def displayPlayersCurrentBalance(self,players):
                for i in range(len(players)):
                        print("Player "+ str(players[i].playerName) + " current balance is: £" + str(players[i].playerBank))
                pass
        def perRoundInfo(self,Round,players):
                print("\n--------------")
                print("Round:",Round)
                self.displayPlayersCurrentBalance(players)
        def blackJackWin(self):
                print("That is Black Jack!")
                pass
        def bust(self,handValue,playerName):
                print(playerName,"hand's value of",handValue,"is a bust :(")
        def betGain(self,playerName,betTotal):
                print("Player",playerName,"has won £" + str(betTotal))
                pass
        def ifBetValid(self,state,betTotal):
                if (state and betTotal > 0):
                        print("Player has placed a bet of: £" + str(betTotal))
                elif (state and betTotal == 0):
                        print("Player has left the table!")
                else:
                        print("Your bet of: £" + str(betTotal) + " is not valid due to insufficient funds; please try again")
                pass
        def naturalBlackJack(self,playerName):
                print("Natural Black Jack! Player",playerName,"wins!")
                pass
        #Dealer Prompts
        def dealerShowsHand(self,dealerHand):
                print("Dealer shows their cards")
                self.displayGivenHand(dealerHand)
                pass
        def dealerStick(self):
                print("Dealer sticks")
                pass
        def dealerBust(self):
                print("Dealer has bust")
                pass
        def displayComparehands(self):
                print("comparing hands")
                pass
        #end of round outcomes
        def roundFinished(self):
                print("All players' round is complete; dealer begins play")
                pass   
        def playerTurn(self,playerName):
                print("Player",playerName,"turn")
                pass
        def playerDoubleDown(self,playerName):
                print("Player",playerName,"has doubled down")
                pass
        def invalidOption(self):
                print("Invalid option, please try again")
                pass
        def surrenderHand(self,playerName):
                print("Player",playerName,"has surrendered their hand")
                pass
        def beatenByDealer(self,playerName):
                print("Player",playerName,"has been beaten by the dealer")
                pass
        def pushTwentyTwo(self,playerName):
                print("Push 22!")
                print(playerName,"you went bust; but you get your money back!")
                pass
        def userBustLose(self,playerName):
                print("Player",playerName,"has lost their bet")
                pass
        def userDraw(self,playerName):
                print("Player",playerName,"has drawn with the dealer")
                print("bet returned")
                pass
        def userWin(self,playerName):
                print("Player",playerName,"has beat the dealer and won their bet")
                pass
        def nonNaturalBlackJack(self,playerName):
                print("Player",playerName,"has won with a Black Jack")
                pass
        #end game message
        def endGame(self):
                print("All players have left the table. Have a great day!")
                pass
        

    
