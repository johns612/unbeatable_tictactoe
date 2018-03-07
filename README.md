# Unbeatable Tic Tac Toe - Python
### A python tic tac toe game with unbeatable minimax based ai.
Note: this was developed in and must be run in Python 2.7.

## HOW TO PLAY:
The object of Tic Tac Toe is to get three in a row. You play on a three by three game board. The first player is known as X and the second is O. Players alternate placing Xs and Os on the game board until either opponent has three in a row or all nine squares are filled.
## MY PROJECT:
My rendition of tic tac toe uses the python shell command prompt for user input and then displays the current state of the game board using the turtle graphics module. When the program starts, the user is given the option to play one or two players.
## TWO PLAYER:
If two player is chosen, the game will cycle back and forth between placing X's and O's, prompting for the user for each move. When an end game state is reached (either X or O wins, or all spaces are filled resulting in a draw/cat's game), the user will be prompted if they would like to play again, quit, or return to the main menu.
## SINGLE PLAYER:
If one player is chosen, the user will then be prompted if they would like to play as X or O, then they will be asked what difficulty the would like the computer to play at: easy, hard, or unbeatable. The game will then cycle back and forth until an end game state is reached.
## EASY MODE:
In this mode, the computer will simply choose a random square from the available squares; no real strategy.
## HARD MODE:
In this mode, the computer will prioritize spots where victory is imminent for either team. So if there are two in a row for either side it will try to complete/block that row. Otherwise it places randomly in an available square.
## UNBEATABLE MODE (Minimax):
This mode uses the minimax algorithm to calculate and store every possible move from both sides, and then filters through these possibilities and determines the best possible move to make based on the current board state. A perfect player will tie with this algorithm every single time, regardless of who starts. I discovered, learned about, and adapted the minimax algorithm from this website: http://www.neverstopbuilding.com/minimax
