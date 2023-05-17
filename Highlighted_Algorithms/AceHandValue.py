#recursive function to find the optimal value of aces in your hand
def recursionAceCalculation(value):
    if (value <= 21):
        return value
    else:
        #recursively goes through aces to find optimal ones and 11s in your hand
        # minus 10 is the value after subtracting 10 and adding 1 to the value
        return recursionAceCalculation(value-10)
    
def handValueCalculation(aceQuantity,handValue):
    #Filtering special case where no matter the arrangement of aces; hand is still a bust
    if (handValue != -1):
        lowCase = handValue + (aceQuantity)
        if (lowCase > 21):
            return lowCase
        elif (aceQuantity == 0):
            return handValue
        else:
            #initial highCase is the value of your other cards (handValue) + the number of aces * 11
            #this process is done recursively
            highCase = handValue + (aceQuantity * 11)
            highCaseCal = recursionAceCalculation(highCase)
            return highCaseCal
    else:
        return handValue