"""tictactoe game for 2 players"""

choices = []            # Empty choice array
for x in range(1, 10):        # Adds values to choices available
    choices.append(x)         # Array of 'choices' from 1-9

playerOneTurn = True          # Determines turn
winner = False                # Determines winner


def printBoard(choices):        # Takes in array and makes Tic Tac Toe Board
    print( '\n -----')
    print( '|' + str(choices[0]) + '|' + str(choices[1]) + '|' + str(choices[2]) + '|')
    print( ' -----')
    print( '|' + str(choices[3]) + '|' + str(choices[4]) + '|' + str(choices[5]) + '|')
    print( ' -----')
    print( '|' + str(choices[6]) + '|' + str(choices[7]) + '|' + str(choices[8]) + '|')
    print( ' -----\n')


while winner == False:      # While there's no winner...
    printBoard(choices)

    if playerOneTurn :      # Checks which turn
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:                    # Checks validation of input
        choice = int(input(">> "))
        if choices[choice - 1] == 'X' or choices[choice-1] == 'O':
            print("illegal move, please try again")
            continue
    except:                 # Move exception to be in between where exception is supposed to occur not before
        print("please enter a valid field")
        continue

    if playerOneTurn:
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn       # Used to alternate turns

    for x in range (0,3):       # Loop checking all possible choices
        y = x * 3
        # Checks horizontal
        if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
            winner = True
            printBoard(choices)             # Needed argument
        # Checks vertical
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard(choices)             # Needed argument
        # Checks diagonal
        if((choices[0] == choices[4] and choices[0] == choices[8]) or
            (choices[2] == choices[4] and choices[4] == choices[6])):
            winner = True
            printBoard(choices)             # Needed argument

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")