###########################################################################
########################---CONWAY'S GAME OF LIFE---########################
###########################################################################
#RULES:
#Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by over-population.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

##########---IMPORTS, WINDOW, CONSTANTS, ARRAYS---##########

import time   #imports time function for delays between displays
import random     #imports the random function to allow a random board to seed
import sys      #imports system to allow exit
from tkinter import *   #imports all of the tkinter GUI functions

root = Tk()     #creates the window
canvas = Canvas(root, width = 800, height = 650, bg="black") #sizes the window
canvas.pack(side = TOP)     #packs the canvas of given size into the window
root.wm_title("Conway's Game of Life") #gives the window a title

ROWS = 65   #number of rows in the grid
COLS = 80   #number of columns in the grid
DELAY = 0.2 #to slow down the printing to the screen so it is viewable by the user
GENERATIONS = 10

grid = [] #main grid used
nxtGrid = [] #grid used to hold the next generation

##########---SUBROUTINES---##########
#####################################

##########---RANDOM GRID---##########
#this fills the array with values randomly

def randomGrid(cols, rows, array):
    for i in range(rows):
        arrayRow = []   #a tempory variable to store each column created
        for j in range(cols):
            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):   #checks if it is the edge box, in order to create the border
                arrayRow += [-1]
            else:
                ran = random.randint(0,3) #between 0 and 3 to have greater chance of of not spawning
                if ran == 0:
                    arrayRow += [1]    #one represents a populated cell
                else:
                    arrayRow += [0]    #zero represents a empty cell
        array += [arrayRow]

##########---GRID CLICK---##########
#the response to a button being clicked

def gridClick(event):
    row = event.y//10
    cols = event.x//10
    if grid[row][cols] == 1:
        grid[row][cols] = 0
        printGrid(COLS, ROWS)      
    elif grid[row][cols] == 0:
        grid[row][cols] = 1
        printGrid(COLS, ROWS)

##########---PRINT GRID---##########
#This prints the grid, either as text to the console or to the GUI (uncomment as applicable
    
def printGrid(cols, rows):
    global grid
    canvas.delete("all")
    canvas.bind("<Button-1>", gridClick)
    #canvas.pack()
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == -1:
                canvas.create_rectangle(10*x, 10*y, 10*x+10, 10*y+10, outline="black", fill="black") #creates black border
            elif grid[y][x] == 1:
                canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="green") #shows populated cell as a green circle
            else:
                canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black") #shows unpopulated cell as a black circle

##########---NEXT GRID---##########
#fills the next grid, to prevent issues with changing current grid as checks are made

def nextGrid(cols, rows, nxt, grid):
    for y in range(1,rows-1):
        for x in range(1,cols-1):
            lives = neighbours(x, y, grid)
            if grid[y][x] == 1 and lives < 2:
                nxt[y][x] = 0
            if grid[y][x] == 1 and (lives == 2 or lives == 3):
                nxt[y][x] = 1
            if grid[y][x] == 1 and lives > 3:
                nxt[y][x] = 0
            if grid[y][x] == 0 and lives == 3:
                nxt[y][x] = 1

##########---NEIGHBOURS---##########
#checks how many neighbours a cell has and follows the rules to change its value if applicable

def neighbours(b, a, grid):
    counter = 0      #counts the number of neighbours
    if grid[a-1][b+1] == 1:
        counter = counter + 1
    if grid[a][b+1] == 1:
        counter = counter + 1
    if grid[a+1][b+1] == 1:
        counter = counter + 1
    if grid[a-1][b] == 1:
        counter = counter + 1
    if grid[a+1][b] == 1:
        counter = counter + 1
    if grid[a-1][b-1] == 1:
        counter = counter + 1
    if grid[a][b-1] == 1:
        counter = counter + 1
    if grid[a+1][b-1] == 1:
        counter = counter + 1
    return counter
    
##########---STEP---##########
#runs one generation change

def step(cols, rows, gens):
    for i in range (0, gens):
        global grid
        global nxtGrid
        nextGrid(cols, rows, nxtGrid, grid)
        grid = nxtGrid
        nxtGrid = grid
        printGrid(cols, rows)
        canvas.update()

def clear(cols, rows):
    global grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                grid[i][j] = 0
    printGrid(cols, rows)
    

########################---MAIN---########################

randomGrid(COLS, ROWS, grid)  #spawns the grid randomly
randomGrid(COLS, ROWS, nxtGrid)  #used to simply fill the grid with the correct number of spaces
printGrid(COLS, ROWS)

Button(root, text='Exit',command=root.destroy).pack(side=BOTTOM)
Button(root, text='Run',command=lambda: step(COLS, ROWS, GENERATIONS)).pack(side=BOTTOM)

Button(root, text='Clear',command=lambda: clear(COLS, ROWS)).pack(side=BOTTOM)

root.mainloop()
