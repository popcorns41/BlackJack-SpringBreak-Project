##Ascii representation methods from src: https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards

specialValueIndex = {
        0:"A",
        1:"2",
        2:"3",
        3:"4",
        4:"5",
        5:"6",
        6:"7",
        7:"8",
        8:"9",
        9:"10",
        10:"J",
        11:"Q",
        12:"K"    
    }

def valueStr(v):
    return specialValueIndex[v]

def ascii_version_of_card(cards,return_string=True):

        # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]
        for card in cards:
            if (card.reveal):
                # "King" should be "K" and "10" should still be "10"
                if card.value == 9:  # ten is the only one who's rank is 2 char long
                        rank = valueStr(card.value)
                        space = ''  # if we write "10" on the card that line will be 1 char to long
                else:
                        rank = valueStr(card.value)  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
                        space = ' '  # no "10", we use a blank space to will the void
                    # get the cards suit in two steps
                suit = card.suitSymbol

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