
def colourStr(c):
    return "Red" if c == True else "Black"


def suitSymbol(s):
    match s:
        case "Clubs":
            return '♣'
        case "Diamonds":
            return '♦'
        case "Hearts":
            return '♥'
        case "Spades":
            return '♠'
        case other:
            return "N/A"

