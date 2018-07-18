# Unbeatable Tic Tac Toe - Python
### A python tic tac toe game with unbeatable minimax based ai.

I've turned this program into a web app! [Try it now!](http://kraylus.cloud/public/game/tic-tac-toe.html)

Note: This game was developed as the final project for my Computer Science 101 class as a freshman in college. I'm fully aware that there are some pretty awful practices in use here (spaghetti code, awful UX, etc.), but I like to remind myself where I started. That being said, the code works like a charm so feel free to download it and try it out for yourself. Perhaps someday I'll create a cleaner version with better coding standards.

## RUNNING THE GAME
Make sure you have Python 2.7 installed on your machine as well as the turtle graphics module installed. Once this is done, simply run the following in your command line from with the repository.
```
python game.py
```
This will cause a turtle graphics window to appear and the main menu will display in your command line window.

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
## AVAILABLE COMMANDS
* tl = top-left
* tm = top-middle
* tr = top-right
* ml = mid-left
* mm = mid-middle
* mr = mid-right
* bl = bot-left
* bm = bot-middle
* br = bot-right
* restart = start over
* quit = exit game
* com = show commands
* main = go to main menu
