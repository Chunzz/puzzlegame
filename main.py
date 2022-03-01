import random


randomNumber = random.randint(1,9)
operators = ["+", "-", "*", "/"]

# print(randomNumber)

grid = []

def createGrid(gridSize):
    for i in range(gridSize):
        gridRow = []
        for j in range(gridSize):
            randomNumber = random.randint(1,9)
            gridRow.append(randomNumber)

        grid.append(gridRow)

createGrid(3)
# print(grid)

def printGrid(grid):
    for i in range(len(grid)):
        string = ""
        for j in range(len(grid)):
            string += str(grid[i][j]) + " "

            if j != len(grid)-1:
                randomOperator = operators[random.randint(0,3)] + " "
                string += randomOperator

        print(string)

        if i != len(grid)-1:
            string = ""
            randomOperator = operators[random.randint(0, 3)] + "   "
            string += randomOperator
            randomOperator = operators[random.randint(0, 3)] + "   "
            string += randomOperator
            randomOperator = operators[random.randint(0, 3)] + "    "
            string += randomOperator
            print(string)

# printGrid(grid)