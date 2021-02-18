

# '''
#     we are going to make a tic-tac-toc game, you will be playing against the computer. but it is gonna be really hard to win. 
#     The user will play as x. Every round, they will pick where they want to put an x, the the computer eil place an o.
#     we need to chek if there is a winer or there is a tie.
#     we also need to make shur there is not two x or o in the same spot

# '''


# steps to follow

# 1 create a turtle an a function that draw the background
# 2 create a function to draw an x and an o
# 3 create event listeners
# 4 create a representation of the board in the code.
# 5 create a turtle to set information in the screen and tell the player if they pick up an invalid spot.
# 6 cerate a function to chek if they won and put it in the right place.
# 7 create a function to put the o of the computer
# 8 check if o won
# 9 function to chek for a tie

import turtle
import math
# all the functions in the beggining

# funtion to draw the grid the game will bve play on it
def drawBoard():
    # draw the two horizontal lines from differents heights
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    # draw both of the vertical lines

    for i in range(2):
        drawer.penup()
        drawer.goto(-100 +200 *i , 300)
        drawer.pendown()
        drawer.forward(600)

    # add numbers to the top of the squares
    number = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()

            drawer.write(number, font= ("Arial", 12))
            number += 1
    # update the screen with new changes
    screen.update()


# this function draw an x centered in the imputed coordinates
def draX(x, y):
    # move to the correct spot
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(60)

    # draw the lines of the x
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    # update the screen
    screen.update()

def draO(x, y):
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)

    # draw a circle with the correct size

    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)
    
    # update the screen
    screen.update()

# this function will check if the inputted player has won 
def checkWon(letter):
    # check for the horizontall or verticall wining
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True


        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board [0][i] == letter:
            return True


    # chek for the diagonall wining
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
        return True

    # if at this point there is no won
    return False
    
# function to check if the game is a tie
def checkDraw():
    # count the number of x on the board
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count += 1

    # check the value of count  
    if count > 3:
        return True
    else:
        return False

# function to add an o in the board in the best place possible.

def addO():
    # first chek if any place is gonna be a win for o
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                if checkWon("o"):
                    draO(-200 + 200 * j , 200 -200 * i)
                    return
                board[i][j] = " "


    # check if we need to block x in any place
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    draO(-200 + 200 * j, 200 - 200 * i )
                    return
                board[i][j] = " "


    # place an o in one of the corners
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j] = "o"
                draO(-200 + 200 * j, 200 - 200 * i)
                return

    # place an "o" in any empty spot
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                draO(-200 + 200 * j, 200 - 200 * i)
                return




# this functions activate all the event listeners
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i + 1))

# this function desactivate all the event listeners
def desactivate():
    for i in range(9):
        screen.onkey(None, str(i + 1))

# function to add the x in to the inputted location

def addX(row, column):
    # clear any announcement in the screen
    announcer.clear()
    #   firs check if the spot they want to add is occupied
    if board[row][column] == "x" or board[row][column] == "o":
        # tell the user that spot is occupied
        announcer.write("That spot is already taken", font= ("Arial", 36))
        screen.update()
    else:
        # draw the x in the correct spot
        draX(-200 + 200 * column, 200 -200 * row)

        # add an x to the computers board
        board[row][column] = "x" 

        # check if the new x made win
        if checkWon("x"):
            # thell the user he won
            announcer.goto(-97, 0)
            announcer.write("You Won.", font= ("Arial", 36))
            # update the screen and desactivate the event listeners.
            screen.update()
            desactivate()
        else:
            addO()

            # check if now o won
            if checkWon("o"):
                # tell the player they lost
                announcer.goto(-90, 0)
                announcer.write("you lost", font = ("Arial", 36))

                # update the screen and desactivate the listeners
                screen.update()
                desactivate()
                
            # check if there was a tie
            elif checkDraw():
                # tell the player they tie
                announcer.goto(-90, 0)
                announcer.write("It is a tie game", font = ("Arial", 36))

                # update the screen and desactivate the listeners
                screen.update()
                desactivate()



        
        

        


# define functions for the events listeners

def squareOne():
    addX(0, 0)

def squareTwo():
    addX(0, 1)

def squareThree():
    addX(0, 2)

def squareFour():
    addX(1, 0)

def squareFive():
    addX(1, 1)

def squareSix():
    addX(1, 2)

def squareSeven():
    addX(2, 0)

def squareEight():
    addX(2, 1)

def squareNine():
    addX(2, 2)


# create a list of event listener functions

functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]






# create turtle

drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht() # hide the turtle

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")




# create screen

screen = turtle.Screen()
screen.tracer(0)


# draw the board
drawBoard()

# create the board

board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)


# activates the event listeners
activate(functions)
screen.listen()


input("press enter to close")