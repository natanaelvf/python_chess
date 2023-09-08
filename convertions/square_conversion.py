def square_string_to_binary(square):
    # Empty squares
    if square == " ":
        return 0
    
    # Black pieces
    elif square == "p":
        return 1
    elif square == "k":
        return 6
    elif square == "q":
        return 5
    elif square == "r":
        return 4

    # White pieces
    elif square == "P":
        return 9
    elif square == "K":
        return 14
    elif square == "R":
        return 12
    elif square == "Q":
        return 13

    match square:
        case "b":
            return 3
        case "B":
            return 11
        case "n":
            return 2
        case "N":
            return 10
        
def square_binary_to_string(square):
    # Empty squares
    if square == 0:
        return " "
    
    # Black pieces
    elif square == 1:
        return "p"
    elif square == 6:
        return "k"
    elif square == 5:
        return "q"
    elif square == 4:
        return "r"
    
    # White pieces
    elif square == 9:
        return "P"
    elif square == 14:
        return "K"
    elif square == 12:
        return "R"
    elif square == 13:
        return "Q"

    # Bishops and knights have approximately the same frequency
    match square:
        case 3:
            return "b"
        case 11:
            return "B"
        case 2:
            return "n"
        case 10:
            return "N"