#CPCS 230-06 Final Project
#Name: William Shevis Johnson
#Date: 11/20/14
#Description: Tic Tac Toe game, using a combination of command line and turtle graphics. Has player v player and player v computer with three different computer difficulty levels.

from turtle import *
from random import randint
import copy

#draws a new board
def newBoard():
    clear()
    up()
    goto(-50,150)
    setheading(270)
    down()
    a = 0
    for a in range(3):
        forward(300)
        left(180)
        forward(100)
        left(90)
        forward(100)
        left(180)
        a += 1
    forward(300)
    up()

#Draws an O
def drawO():
    color("blue")
    setheading(90)
    forward(44.1963)
    left(90)
    forward(7)
    setheading(180)
    b = 0
    for b in range(20):
        down()
        left(18)
        forward(14)
        b += 1
    color("black")
    up()

#Draws an X
def drawX():
    color("red")
    down()
    setheading(45)
    c = 0
    for c in range(4):
        forward(64)
        backward(64)
        left(90)
        c += 1
    color("black")
    up()

#Draws lines indicating victory
def topRow():
    color("green")
    goto(-150,100)
    down()
    goto(150,100)
    color("black")
    up()
def midRow():
    color("green")
    goto(-150,0)
    down()
    goto(150,0)
    color("black")
    up()
def botRow():
    color("green")
    goto(-150,-100)
    down()
    goto(150,-100)
    color("black")
    up()
def leftCol():
    color("green")
    goto(-100,150)
    down()
    goto(-100,-150)
    color("black")
    up()
def midCol():
    color("green")
    goto(0,150)
    down()
    goto(0,-150)
    color("black")
    up()
def rightCol():
    color("green")
    goto(100,150)
    down()
    goto(100,-150)
    color("black")
    up()
def downUpDiag():
    color("green")
    goto(-150,-150)
    down()
    goto(150,150)
    color("black")
    up()
def upDownDiag():
    color("green")
    goto(-150,150)
    down()
    goto(150,-150)
    color("black")
    up()

def checkString(s):
    try:
        str(s)
        return True
    except ValueError:
        return False

def checkInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Runs restart cycle
def restart():
    while True:
        playAgain = raw_input("\nWould you like to play again? (y/n or type 'main' to return to main menu): ")
        try:
            str(playAgain)
            if playAgain.lower() == "y":
                print"\nPlease wait while a new board is drawn..."
                newBoard()
                return 1
                break
            elif playAgain.lower() == "n":
                return 0
                break
            elif playAgain.lower() == "main":
                return 2
                break
            else:
                print"\nInvalid Input"
        except ValueError:
            print"\nInvalid Input"

#Main Menu cycle, returns what the user would like to do.
def mainMenu():
    layer = True
    print"\nMAIN MENU\n\n1 = Start single player game\n2 = Start two player game\ncom = view game commands\nquit = quit"
    while layer == True:
        numOfPlayers = raw_input("\nWhat would you like to do?: ")
        if checkInt(numOfPlayers) == True:
            numOfPlayers_int = int(numOfPlayers)
            if numOfPlayers_int == 1:
                #Set Single Player
                while True:
                    xoro_str = raw_input("\nWould you like to be X's or O's? (X/O): ")
                    if checkString(xoro_str) == True:
                        if xoro_str.lower() == "x":
                            layer = False
                            return 11
                            break
                        elif xoro_str.lower() == "o":
                            layer = False
                            return 10
                            break
                        else:
                            print "\nInvalid Input"
                    else:
                        print "\nInvalid Input"
            elif numOfPlayers_int == 2:
                #Set Double Player
                return 2
                break
            else:
                print"\nInvalid Input"
        elif numOfPlayers == "quit":
            return 0
            break
        elif numOfPlayers == "com":
            print"\nGame Commands:\n", \
                         "tl = top-left\ntm = top-center\ntr = top-right\n", \
                         "ml = mid-left\nmm = mid-center\nmr = mid-right\n", \
                         "bl = bot-left\nbm = bot-center\nbr = bot-right\n", \
                         "restart = start over\nquit = exit game\ncom = show commands\nmain = go to main menu"
        else:
            print"\nInvalid Input"

#EASY MODE: Returns a random available square
def findBestChoiceEasy():
    while True:
        randInt = randint(0,8)
        if board[randInt] == " ":
            return randInt

#HARD MODE: Finishes lines of 3 or blocks opponent lines of 3, otherwise returns random available space
def findBestChoiceHard():
    if (board[2] == "X" and board[1] == "X" and board[0] == " ") or (board[2] == "O" and board[1] == "O" and board[0] == " "):
        return 0
    elif (board[2] == "X" and board[0] == "X" and board[1] == " ") or (board[2] == "O" and board[0] == "O" and board[1] == " "):
        return 1
    elif (board[1] == "X" and board[0] == "X" and board[2] == " ") or (board[1] == "O" and board[0] == "O" and board[2] == " "):
        return 2
    elif (board[5] == "X" and board[4] == "X" and board[3] == " ") or (board[5] == "O" and board[4] == "O" and board[3] == " "):
        return 3
    elif (board[5] == "X" and board[3] == "X" and board[4] == " ") or (board[5] == "O" and board[3] == "O" and board[4] == " "):
        return 4
    elif (board[4] == "X" and board[3] == "X" and board[5] == " ") or (board[4] == "O" and board[3] == "O" and board[5] == " "):
        return 5
    elif (board[8] == "X" and board[7] == "X" and board[6] == " ") or (board[8] == "O" and board[7] == "O" and board[6] == " "):
        return 6
    elif (board[8] == "X" and board[6] == "X" and board[7] == " ") or (board[8] == "O" and board[6] == "O" and board[7] == " "):
        return 7
    elif (board[7] == "X" and board[6] == "X" and board[8] == " ") or (board[7] == "O" and board[6] == "O" and board[8] == " "):
        return 8

    elif (board[3] == "X" and board[6] == "X" and board[0] == " ") or (board[3] == "O" and board[6] == "O" and board[0] == " "):
        return 0
    elif (board[0] == "X" and board[6] == "X" and board[3] == " ") or (board[0] == "O" and board[6] == "O" and board[3] == " "):
        return 3
    elif (board[0] == "X" and board[3] == "X" and board[6] == " ") or (board[0] == "O" and board[3] == "O" and board[6] == " "):
        return 6
    elif (board[4] == "X" and board[7] == "X" and board[1] == " ") or (board[4] == "O" and board[7] == "O" and board[1] == " "):
        return 1
    elif (board[1] == "X" and board[7] == "X" and board[4] == " ") or (board[1] == "O" and board[7] == "O" and board[4] == " "):
        return 4
    elif (board[1] == "X" and board[4] == "X" and board[7] == " ") or (board[1] == "O" and board[4] == "O" and board[7] == " "):
        return 7
    elif (board[5] == "X" and board[8] == "X" and board[2] == " ") or (board[5] == "O" and board[8] == "O" and board[2] == " "):
        return 2
    elif (board[2] == "X" and board[8] == "X" and board[5] == " ") or (board[2] == "O" and board[8] == "O" and board[5] == " "):
        return 5
    elif (board[2] == "X" and board[5] == "X" and board[8] == " ") or (board[2] == "O" and board[5] == "O" and board[8] == " "):
        return 8

    elif (board[4] == "X" and board[2] == "X" and board[6] == " ") or (board[4] == "O" and board[2] == "O" and board[6] == " "):
        return 6
    elif (board[6] == "X" and board[2] == "X" and board[4] == " ") or (board[6] == "O" and board[2] == "O" and board[4] == " "):
        return 4
    elif (board[4] == "X" and board[6] == "X" and board[2] == " ") or (board[4] == "O" and board[6] == "O" and board[2] == " "):
        return 2

    elif (board[4] == "X" and board[0] == "X" and board[8] == " ") or (board[4] == "O" and board[0] == "O" and board[8] == " "):
        return 8
    elif (board[8] == "X" and board[0] == "X" and board[4] == " ") or (board[8] == "O" and board[0] == "O" and board[4] == " "):
        return 4
    elif (board[4] == "X" and board[8] == "X" and board[0] == " ") or (board[4] == "O" and board[8] == "O" and board[0] == " "):
        return 0

    else:
        while True:
            randInt = randint(0,8)
            if board[randInt] == " ":
                return randInt

#Returns an array of all available moves in a given board state.
def getPossibleMoves(a_board):
    pMoves = []
    for i in range(0, 9):
        if a_board[i] == " ":
            pMoves.append(i)
    return pMoves

#Checks if either X or O has won a given board state.
def checkWon(a_board, symbol):
    if ((a_board[0] == symbol and a_board[1] == symbol and a_board[2] == symbol) or
       (a_board[3] == symbol and a_board[4] == symbol and a_board[5] == symbol) or
       (a_board[6] == symbol and a_board[7] == symbol and a_board[8] == symbol) or
       (a_board[0] == symbol and a_board[3] == symbol and a_board[6] == symbol) or
       (a_board[1] == symbol and a_board[4] == symbol and a_board[7] == symbol) or
       (a_board[2] == symbol and a_board[5] == symbol and a_board[8] == symbol) or
       (a_board[0] == symbol and a_board[4] == symbol and a_board[8] == symbol) or
       (a_board[2] == symbol and a_board[4] == symbol and a_board[6] == symbol)):
          return True
    else:
        return False

#Scoring for minimax algorithm
def score(a_board, depth):
    if checkWon(a_board, player):
        return 10 - depth
    if checkWon(a_board, opp):
        return depth - 10
    else:
        return 0

#returns the index of the max value of an array
def findMaxVal(a_list):
    maxVal = -100
    for i in range(len(a_list)):
        if a_list[i] > maxVal:
            maxVal = a_list[i]
            index = i
    return index

#returns the index of the minimum value of an array
def findMinVal(a_list):
    minVal = 100
    for i in range(len(a_list)):
        if a_list[i] < minVal:
            minVal = a_list[i]
            index = i
    return index

#UNBEATABLE MODE: Calculates and stores every possible game state and sets the_move to be the best possible move for a given board
def Minimax(a_board, value, depth, symbol):
    if checkWon(a_board, player) or checkWon(a_board, opp) or getPossibleMoves(a_board) == []:
        return value
    depth += 1
    scores = []
    moves = getPossibleMoves(a_board)
    newSymbol = copy.deepcopy(symbol)
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X"

    for i in moves:
        copyBoard = copy.deepcopy(a_board)
        copyBoard[i] = newSymbol
        copyValue = score(copyBoard, depth)
        scores.append(Minimax(copyBoard, copyValue, depth, symbol))

    if newSymbol == player:
        global the_move
        maxScoreIndex = findMaxVal(scores)
        the_move = moves[maxScoreIndex]
        return scores[maxScoreIndex]
    else:
        minScoreIndex = findMinVal(scores)
        return scores[minScoreIndex]

redTurn = True
board = [" "] * 9
resetGame = False
gameIsOver = False
layerTwo = True
numberOfPlayers = 1
i_depth = 0
the_move = 3

#INSTRUCTIONS
print"TIC, TAC, TOE GAME\n", \
           "\nHOW TO PLAY:\n" \
           "The object of Tic Tac Toe is to get three in a row.\n", \
           "You play on a three by three game board. The first\n", \
           "player is known as X and the second is O. Players\n", \
           "alternate placing Xs and Os on the game board until\n", \
           "either oppent has three in a row or all nine squares\n", \
           "are filled.\n\n", \
           "Game Commands:\n", \
           "tl = top-left\ntm = top-middle\ntr = top-right\n", \
           "ml = mid-left\nmm = mid-middle\nmr = mid-right\n", \
           "bl = bot-left\nbm = bot-middle\nbr = bot-right\n", \
           "restart = start over\nquit = exit game\ncom = show commands\n", \
           "main = go to main menu\n\nPlease wait while the board is drawn..."

newBoard()

#overlying game loop. Only breaks if game is quitting.
while layerTwo == True:

    #Setup for game
    main = mainMenu()
    if main == 2:
        numberOfPlayers = 2
    elif main == 11:
        numberOfPlayers = 1
        isUserMove = True
        userIsX = True
        playerSymbol = "X"
        comSymbol = "O"
    elif main == 10:
        numberOfPlayers = 1
        isUserMove = False
        userIsX = False
        playerSymbol = "O"
        comSymbol = "X"
    elif main == 0:
        print"\nGoodbye!"
        break

    #2 PLAYER MODE
    if numberOfPlayers == 2:
        #Turn loop
        while True:
            if redTurn == True:
                print"\nPLAYER 1 (X)"
            else:
                print"\nPLAYER 2 (O)"

            #User Input for move
            move_raw = raw_input("Please enter your move: ")

            if checkString(move_raw) == True:
                userMove_str = str(move_raw)
                if userMove_str.lower() == "tl":
                    goto(-100,100)
                    if redTurn == True:
                        if board[0] == " ":
                            drawX()
                            board[0] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[0] == " ":
                            drawO()
                            board[0] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "tm":
                    goto(0,100)
                    if redTurn == True:
                        if board[1] == " ":
                            drawX()
                            board[1] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[1] == " ":
                            drawO()
                            board[1] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "tr":
                    goto(100,100)
                    if redTurn == True:
                        if board[2] == " ":
                            drawX()
                            board[2] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[2] == " ":
                            drawO()
                            board[2] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "ml":
                    goto(-100,0)
                    if redTurn == True:
                        if board[3] == " ":
                            drawX()
                            board[3] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[3] == " ":
                            drawO()
                            board[3] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "mm":
                    goto(0,0)
                    if redTurn == True:
                        if board[4] == " ":
                            drawX()
                            board[4] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[4] == " ":
                            drawO()
                            board[4] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "mr":
                    goto(100,0)
                    if redTurn == True:
                        if board[5] == " ":
                            drawX()
                            board[5] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[5] == " ":
                            drawO()
                            board[5] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "bl":
                    goto(-100,-100)
                    if redTurn == True:
                        if board[6] == " ":
                            drawX()
                            board[6] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[6] == " ":
                            drawO()
                            board[6] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "bm":
                    goto(0,-100)
                    if redTurn == True:
                        if board[7] == " ":
                            drawX()
                            board[7] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[7] == " ":
                            drawO()
                            board[7] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "br":
                    goto(100,-100)
                    if redTurn == True:
                        if board[8] == " ":
                            drawX()
                            board[8] = "X"
                            redTurn = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[8] == " ":
                            drawO()
                            board[8] = "O"
                            redTurn = True
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "quit":
                    print"\nGoodbye!"
                    layerTwo = False
                    break
                elif userMove_str.lower() == "com":
                    print"\nGame Commands:\n", \
                               "tl = top-left\ntm = top-center\ntr = top-right\n", \
                               "ml = mid-left\nmm = mid-center\nmr = mid-right\n", \
                               "bl = bot-left\nbm = bot-center\nbr = bot-right\n", \
                               "restart = start over\nquit = exit game\ncom = show commands\nmain = go to main menu"
                elif userMove_str.lower() == "restart":
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    resetGame = True
                elif userMove_str.lower() == "main":
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    resetGame = True
                    break
                else:
                    print"\nInvalid Input"
            else:
                print"\nInvalid Input"

            #WIN CONDITIONS

            #X
            #Rows
            if board[0] == "X" and board[1] == "X" and board[2] == "X":
                print"\nX WINS!"
                topRow()
                gameIsOver = True
            elif board[3] == "X" and board[4] == "X" and board[5] == "X":
                print"\nX WINS!"
                midRow()
                gameIsOver = True
            elif board[6] == "X" and board[7] == "X" and board[8] == "X":
                print"\nX WINS!"
                botRow()
                gameIsOver = True
            #Columns
            elif board[0] == "X" and board[3] == "X" and board[6] == "X":
                print"\nX WINS!"
                leftCol()
                gameIsOver = True
            elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                print"\nX WINS!"
                midCol()
                gameIsOver = True
            elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                print"\nX WINS!"
                rightCol()
                gameIsOver = True
            #Diagonals
            elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                print"\nX WINS!"
                upDownDiag()
                gameIsOver = True
            elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                print"\nX WINS!"
                downUpDiag()
                gameIsOver = True
            #O
            #Rows
            if board[0] == "O" and board[1] == "O" and board[2] == "O":
                print"\nO WINS!"
                topRow()
                gameIsOver = True
            elif board[3] == "O" and board[4] == "O" and board[5] == "O":
                print"\nO WINS!"
                midRow()
                gameIsOver = True
            elif board[6] == "O" and board[7] == "O" and board[8] == "O":
                print"\nO WINS!"
                botRow()
                gameIsOver = True
            #Columns
            elif board[0] == "O" and board[3] == "O" and board[6] == "O":
                print"\nO WINS!"
                leftCol()
                gameIsOver = True
            elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                print"\nO WINS!"
                midCol()
                gameIsOver = True
            elif board[2] == "O" and board[5] == "O" and board[8] == "O":
                print"\nO WINS!"
                rightCol()
                gameIsOver = True
            #Diagonals
            elif board[0] == "O" and board[4] == "O" and board[8] == "O":
                print"\nO WINS!"
                upDownDiag()
                gameIsOver = True
            elif board[2] == "O" and board[4] == "O" and board[6] == "O":
                print"\nO WINS!"
                downUpDiag()
                gameIsOver = True
            #CAT'S GAME
            elif (board[0] == "X" or board[0] == "O") and (board[1] == "X" or board[1] == "O") and \
                 (board[2] == "X" or board[2] == "O") and (board[3] == "X" or board[3] == "O") and \
                 (board[4] == "X" or board[4] == "O") and (board[5] == "X" or board[5] == "O") and \
                 (board[6] == "X" or board[6] == "O") and (board[7] == "X" or board[7] == "O") and \
                 (board[8] == "X" or board[8] == "O") and checkWon(board, "X") == False and checkWon(board, "O") == False:
                print"\nCAT'S GAME!"
                gameIsOver = True
            if gameIsOver == True:
                playAgain = restart()
                if playAgain == False:
                    print"\nGoodbye!"
                    layerTwo = False
                    break
                elif playAgain == 2:
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    redTurn = True
                    board = [" "] * 9
                    resetGame = False
                    gameIsOver = False
                    break
                else:
                    resetGame = True
            if resetGame == True:
                redTurn = True
                board = [" "] * 9
                resetGame = False
                gameIsOver = False

    #1 PLAYER MODE
    elif numberOfPlayers == 1:
        firstTurn = True

        #Set computer difficulty
        while True:
            print"\nCOMPUTER DIFFICULTY LEVEL\n1 = Easy\n2 = Hard\n3 = Unbeatable"
            level_raw = raw_input("\nPlease choose a difficulty level: ")
            if checkInt(level_raw) == True and int(level_raw) <= 3:
                level = int(level_raw)
                break
            else:
                print"\nInvalid Input"

        #Turn Loop
        while True:
            if redTurn == True and isUserMove == True:
                print"\nUSER (X)"
            elif redTurn == False and isUserMove == True:
                print"\nUSER (O)"
            elif redTurn == True and isUserMove == False:
                print"\nCOMPUTER (X)"
                opp = "O"
                player = "X"
            else:
                print"\nCOMPUTER (O)"
                player = "O"
                opp = "X"
            if isUserMove == True:
                move_raw = raw_input("Please enter your move: ")
            else:
                #EASY MODE
                if level == 1:
                    computerChoice = findBestChoiceEasy()
                #HARD MODE
                elif level == 2:
                    computerChoice = findBestChoiceHard()
                #UNBEATABLE MODE
                elif level == 3:
                    print"\nThinking..."
                    if firstTurn:
                        computerChoice = findBestChoiceEasy()
                    else:
                        node = Minimax(board, 0, 0, player)
                        computerChoice = the_move

                #Convert computer move into user input format
                if computerChoice == 0:
                    move_raw = "tl"
                    print"\ntop-left"
                elif computerChoice == 1:
                    move_raw = "tm"
                    print"\ntop-mid"
                elif computerChoice == 2:
                    move_raw = "tr"
                    print"\ntop-right"
                elif computerChoice == 3:
                    move_raw = "ml"
                    print"\nmid-left"
                elif computerChoice == 4:
                    move_raw = "mm"
                    print"\nmid-mid"
                elif computerChoice == 5:
                    move_raw = "mr"
                    print"\nmid-right"
                elif computerChoice == 6:
                    move_raw = "bl"
                    print"\nbot-left"
                elif computerChoice == 7:
                    move_raw = "bm"
                    print"\nbot-mid"
                elif computerChoice == 8:
                    move_raw = "br"
                    print"\nbot-right"

            #Check and play move
            if checkString(move_raw) == True:
                userMove_str = str(move_raw)
                if userMove_str.lower() == "tl":
                    goto(-100,100)
                    if redTurn == True:
                        if board[0] == " ":
                            drawX()
                            board[0] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[0] == " ":
                            drawO()
                            board[0] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "tm":
                    goto(0,100)
                    if redTurn == True:
                        if board[1] == " ":
                            drawX()
                            board[1] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[1] == " ":
                            drawO()
                            board[1] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "tr":
                    goto(100,100)
                    if redTurn == True:
                        if board[2] == " ":
                            drawX()
                            board[2] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[2] == " ":
                            drawO()
                            board[2] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "ml":
                    goto(-100,0)
                    if redTurn == True:
                        if board[3] == " ":
                            drawX()
                            board[3] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[3] == " ":
                            drawO()
                            board[3] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "mm":
                    goto(0,0)
                    if redTurn == True:
                        if board[4] == " ":
                            drawX()
                            board[4] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[4] == " ":
                            drawO()
                            board[4] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "mr":
                    goto(100,0)
                    if redTurn == True:
                        if board[5] == " ":
                            drawX()
                            board[5] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[5] == " ":
                            drawO()
                            board[5] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "bl":
                    goto(-100,-100)
                    if redTurn == True:
                        if board[6] == " ":
                            drawX()
                            board[6] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[6] == " ":
                            drawO()
                            board[6] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "bm":
                    goto(0,-100)
                    if redTurn == True:
                        if board[7] == " ":
                            drawX()
                            board[7] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[7] == " ":
                            drawO()
                            board[7] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "br":
                    goto(100,-100)
                    if redTurn == True:
                        if board[8] == " ":
                            drawX()
                            board[8] = "X"
                            redTurn = False
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                    else:
                        if board[8] == " ":
                            drawO()
                            board[8] = "O"
                            redTurn = True
                            if isUserMove == False:
                                isUserMove = True
                            elif isUserMove == True:
                                isUserMove = False
                        else:
                            print"\nSpace already filled!"
                elif userMove_str.lower() == "quit":
                    print"\nGoodbye!"
                    layerTwo = False
                    break
                elif userMove_str.lower() == "com":
                    print"\nGame Commands:\n", \
                               "tl = top-left\ntm = top-center\ntr = top-right\n", \
                               "ml = mid-left\nmm = mid-center\nmr = mid-right\n", \
                               "bl = bot-left\nbm = bot-center\nbr = bot-right\n", \
                               "restart = start over\nquit = exit game\ncom = show commands\nmain = go to main menu"
                elif userMove_str.lower() == "restart":
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    resetGame = True
                elif userMove_str.lower() == "main":
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    redTurn = True
                    board = [" "] * 9
                    resetGame = False
                    gameIsOver = False
                    firstTurn = True
                    isUserMove = userIsX
                    break
                else:
                    print"\nInvalid Input"
            else:
                print"\nInvalid Input"

            firstTurn = False

            #WIN CONDITIONS

            #X
            #Rows
            if board[0] == "X" and board[1] == "X" and board[2] == "X":
                print"\nX WINS!"
                topRow()
                gameIsOver = True
            elif board[3] == "X" and board[4] == "X" and board[5] == "X":
                print"\nX WINS!"
                midRow()
                gameIsOver = True
            elif board[6] == "X" and board[7] == "X" and board[8] == "X":
                print"\nX WINS!"
                botRow()
                gameIsOver = True
            #Columns
            elif board[0] == "X" and board[3] == "X" and board[6] == "X":
                print"\nX WINS!"
                leftCol()
                gameIsOver = True
            elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                print"\nX WINS!"
                midCol()
                gameIsOver = True
            elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                print"\nX WINS!"
                rightCol()
                gameIsOver = True
            #Diagonals
            elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                print"\nX WINS!"
                upDownDiag()
                gameIsOver = True
            elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                print"\nX WINS!"
                downUpDiag()
                gameIsOver = True
            #O
            #Rows
            if board[0] == "O" and board[1] == "O" and board[2] == "O":
                print"\nO WINS!"
                topRow()
                gameIsOver = True
            elif board[3] == "O" and board[4] == "O" and board[5] == "O":
                print"\nO WINS!"
                midRow()
                gameIsOver = True
            elif board[6] == "O" and board[7] == "O" and board[8] == "O":
                print"\nO WINS!"
                botRow()
                gameIsOver = True
            #Columns
            elif board[0] == "O" and board[3] == "O" and board[6] == "O":
                print"\nO WINS!"
                leftCol()
                gameIsOver = True
            elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                print"\nO WINS!"
                midCol()
                gameIsOver = True
            elif board[2] == "O" and board[5] == "O" and board[8] == "O":
                print"\nO WINS!"
                rightCol()
                gameIsOver = True
            #Diagonals
            elif board[0] == "O" and board[4] == "O" and board[8] == "O":
                print"\nO WINS!"
                upDownDiag()
                gameIsOver = True
            elif board[2] == "O" and board[4] == "O" and board[6] == "O":
                print"\nO WINS!"
                downUpDiag()
                gameIsOver = True
            #CAT'S GAME
            elif (board[0] == "X" or board[0] == "O") and(board[1] == "X" or board[1] == "O") and \
                 (board[2] == "X" or board[2] == "O") and (board[3] == "X" or board[3] == "O") and \
                 (board[4] == "X" or board[4] == "O") and (board[5] == "X" or board[5] == "O") and \
                 (board[6] == "X" or board[6] == "O") and (board[7] == "X" or board[7] == "O") and \
                 (board[8] == "X" or board[8] == "O") and checkWon(board, player) == False and checkWon(board, opp) == False:
                print"\nCAT'S GAME!"
                gameIsOver = True
            if gameIsOver == True:
                playAgain = restart()
                if playAgain == 0:
                    print"\nGoodbye!"
                    layerTwo = False
                    break
                elif playAgain == 2:
                    print"\nPlease wait while a new board is drawn..."
                    newBoard()
                    redTurn = True
                    board = [" "] * 9
                    resetGame = False
                    gameIsOver = False
                    firstTurn = True
                    isUserMove = userIsX
                    break
                else:
                    resetGame = True
            if resetGame == True:
                redTurn = True
                board = [" "] * 9
                resetGame = False
                gameIsOver = False
                firstTurn = True
                isUserMove = userIsX
