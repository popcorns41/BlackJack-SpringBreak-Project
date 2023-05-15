import cardGenerationMethods as cgm
import CardsClub as cc

##Ascii representation methods from src: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

def ascii_version_of_card(cards,return_string=True):
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        :param cards: One or more card objects
        :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
        keep it as a list so that the dealer can add a hidden card in front of the list
        """

        # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]
        for card in cards:
            if (card.reveal):
                # "King" should be "K" and "10" should still be "10"
                if card.value == 9:  # ten is the only one who's rank is 2 char long
                        rank = cgm.valueStr(card.value)
                        space = ''  # if we write "10" on the card that line will be 1 char to long
                else:
                        rank = cgm.valueStr(card.value)  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
                        space = ' '  # no "10", we use a blank space to will the void
                    # get the cards suit in two steps
                suit = cgm.suitSymbol(card.suit)

                # add the individual card on a line by line basis
                lines[0].append('┌─────────┐')
                lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
                lines[2].append('│         │')
                lines[3].append('│         │')
                lines[4].append('│    {}    │'.format(suit))
                lines[5].append('│         │')
                lines[6].append('│         │')
                lines[7].append('│       {}{}│'.format(space, rank))
                lines[8].append('└─────────┘')
            else:
                lines[0].append('┌─────────┐')
                lines[1].append('│░░░░░░░░░│')  
                lines[2].append('│░░░░░░░░░│')
                lines[3].append('│░░░░░░░░░│')
                lines[4].append('│░░░░░░░░░│')
                lines[5].append('│░░░░░░░░░│')
                lines[6].append('│░░░░░░░░░│')
                lines[7].append('│░░░░░░░░░│')
                lines[8].append('└─────────┘')

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))

        # hidden cards do not use string
        if return_string:
            return '\n'.join(result)
        else:
            return result

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
                print(ascii_version_of_card(hand))
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
        def bust(self,handValue):
                print("Your hand's value of",handValue,"is a bust :(")
        def ifBetValid(self,state,betTotal):
                if (state and betTotal > 0):
                        print("Player has placed a bet of: £" + str(betTotal))
                elif (state and betTotal == 0):
                        print("Player has left the table!")
                else:
                        print("Your bet of: £" + str(betTotal) + " is not valid due to insufficient funds; please try again")
                pass
                        

    
