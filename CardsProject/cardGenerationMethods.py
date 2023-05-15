
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
def colourStr(c):
    return "Red" if c == True else "Black"

def valueStr(v):
    return specialValueIndex[v]

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
