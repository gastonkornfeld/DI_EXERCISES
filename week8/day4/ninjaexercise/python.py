


# Exercise 1 : Conway’s Game Of Life
# These are the rules of the Game of Life (as stated in Wikipedia):

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells
# , each of which is in one of two possible states, alive or dead, 
# (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Using these rules, implement the Game. (Hint: use Classes !!!!)
# Use a few different initial states to see how the game ends.

# Notes:
# - Display the grid after each generation
# - The end of the game is fully determined by the initial state. So have it pass through 
# your program and see how it ends.
# - Be creative, but use classes
# - The game can be with fixed borders and can have moving borders. Implement first the fixed 
# borders. Each “live” cell that is going out of the border, exits the game
# - Bonus - Make the game with ever expandable borders, make the maximum border size a very 
# large number(10,000) so you won’t cause a memory overflow







import os
import time
import sys
import random


class Universe():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.contents = {}
        self.generations = 0
        for y in range(self.h):
            for x in range(self.w):
                self.contents[x, y] = 0 
        
        


    def randomize(self):
        out = {}
        self.generation = 1
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 1)
                if c == 0:
                    out[x, y] = 1
                else:
                    out[x, y] = 0
        
        self.contents = out

    def getString(self):
        tostring = ""
        for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x , y]
                if c == 0:
                    tostring += " "
                elif c == 1:
                    tostring += u"\u2588"
            tostring += "\n"
        return tostring
    

    def calculate(self):
        new = {}
        for y in range(self.h):
            for x in range(self.w):
                c = self.contents[x , y]
                u, d, l, r, ur, ul, dr, dl = self.getNeighbours(x, y)
                n = [u, d, l, r, ur, ul, dr, dl]
                n = self.CountNeighbours(n)
                if c == 1:
                    if n > 3:
                        new[x, y] = 0
                    elif n <= 1:
                        new[x, y] = 0
                    elif n == 2 or n == 3:
                        new[x ,y] = 1
                elif c == 0:
                    if n == 3:
                        new[x, y] = 1
                    else:
                        new[x, y] = 0  
        self.contents = new

    def getNeighbours(self, x, y):
        c = self.contents

        try : u = c[x, y-1]
        except: u = 0
        try : d = c[x, y+1]
        except: d = 0
        try : l = c[x-1, y]
        except: l = 0
        try : r = c[x+1, y]
        except: r = 0
        try : ur = c[x+1, y-1]
        except: ur = 0
        try : ul = c[x-1, y-1]
        except: ul = 0
        try : dr = c[x+1, y+1]
        except: dr = 0
        try : dl = c[x-1, y+1]
        except: dl = 0

        return u, d, l, r, ur, ul, dr, dl

    def CountNeighbours(self, n):
        count = 0
        for i in range(len(n)):
            c = n[i]
            if c == 1:
                count += 1
        return count





def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

try:
    WIDTH = int(sys.argv[1])
except:
    WIDTH = 100

try:
    HEIGHT = int(sys.argv[2])
except:
    HEIGHT = 25


try:
    DELAY = float(sys.argv[3])
except:
    DELAY = 0.1

universe = Universe(WIDTH, HEIGHT)
universe.randomize()

while True:
    # clear screen
    cls()
    
    #calculate cell position
    universe.calculate()
    #draw new universe

    print(universe.getString())
    time.sleep(DELAY)