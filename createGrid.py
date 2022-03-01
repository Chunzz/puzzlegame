import random
randomNumber = random.randint(1,9)


operators = ["+", "-", "*", "/"]
operatorPositions = [[0,1],[1,0],[1,2],[2,1]]
numberPositions = [[0,0], [0,2], [2,0], [2,2]]
divisionPositions=[]
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
horizontalSolutions = []
verticalSolutions = []

def createGrid():

    generateOperator(grid)
    generateNumber(grid)
    printGrid(grid)

def generateOperator(grid):
    divisionCount = 0

    for i in range(len(operatorPositions)):
        operatorX = operatorPositions[i][0]
        operatorY = operatorPositions[i][1]

        if divisionCount >= 2:
            operator = operators[random.randint(0,2)]
        else:
            operator = operators[random.randint(0,3)]

        if operator == "/":
            divisionPositions.append([operatorX, operatorY])
            divisionCount+=1
        grid[operatorX][operatorY] = operator

def generateNumber(grid):
    #populate divisions first

    for i in range(len(divisionPositions)):
        divisionX = divisionPositions[i][0]
        divisionY = divisionPositions[i][1]

        if (divisionX == 1) :
            if grid[divisionX-1][divisionY] == 0 and grid[divisionX+1][divisionY] == 0:
                number = random.randint(1, 9)
                grid[divisionX - 1][divisionY] = number
                grid[divisionX + 1][divisionY] = number
            else:
                grid[divisionX - 1][divisionY] = grid[divisionX + 1][divisionY] + grid[divisionX - 1][divisionY]
                grid[divisionX + 1][divisionY] = grid[divisionX + 1][divisionY] + grid[divisionX - 1][divisionY]


        elif (divisionY == 1):
            if grid[divisionX][divisionY-1] == 0 and grid[divisionX][divisionY+1] == 0:
                number = random.randint(1, 9)
                grid[divisionX][divisionY-1] = number
                grid[divisionX][divisionY+1] = number
            else:
                grid[divisionX][divisionY-1] =  grid[divisionX][divisionY+1] + grid[divisionX][divisionY-1]
                grid[divisionX][divisionY + 1] = grid[divisionX][divisionY+1] + grid[divisionX][divisionY-1]

    for i in range(len(numberPositions)):
        numberX = numberPositions[i][0]
        numberY = numberPositions[i][1]

        if (grid[numberX][numberY] == 0):
            number = random.randint(1,9)
            grid[numberX][numberY] = number



def printGrid(grid):
    for i in range(3):
        row = ""
        for j in range(3):
            if grid[i][j] == 0:
                row += " "
            else:
                row += str(grid[i][j])
            row += " "
        print(row)

def printGridWithSolutions(grid, horizontalSolutions, verticalSolutions):
    gridWithSolutions = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]

    for i in range(3):
        for j in range(3):
            if grid[i][j] != 0:
                gridWithSolutions[i+1][j+1] = grid[i][j]

    for i in range(3):
        if (i % 2) == 0:
            gridWithSolutions[i+1][0] = horizontalSolutions[i/2][0]
            gridWithSolutions[i+1][4] = horizontalSolutions[i/2][1]

    for i in range(3):
        if (i % 2) == 0:
            gridWithSolutions[0][i+1] = verticalSolutions[i/2][0]
            gridWithSolutions[4][i+1] = verticalSolutions[i/2][1]

    # print(gridWithSolutions)

    print("\n" *3)
    for i in range(5):
        print("-"*25)
        row = ""
        for j in range(5):
            # print("|" * 25)
            row += str(gridWithSolutions[i][j])
            row += (5-len(str(gridWithSolutions[i][j]))) * " "
        print(row)




def calculate(operator, numberOne, numberTwo):
    #do math
    if (operator == "+"):
        return numberOne + numberTwo
    if (operator == "-"):
        return numberOne - numberTwo
    if (operator == "*"):
        return numberOne * numberTwo
    if (operator == "/"):
        return numberOne / numberTwo

def generateSolution(grid):


    #Solve horizontals
    for i in range(len(grid)):
        solutionOne = 0
        solutionTwo = 0

        if (i % 2) == 0:
            numberOne = grid[i][0]
            operator = grid[i][1]
            numberTwo = grid[i][2]
            solutionTwo = calculate(operator, numberOne, numberTwo)

            numberOne = grid[i][2]
            operator = grid[i][1]
            numberTwo = grid[i][0]
            solutionOne = calculate(operator, numberOne, numberTwo)

            horizontalSolutions.append([solutionOne, solutionTwo])

    # Solve verticals
    for i in range(len(grid)):
        solutionOne = 0
        solutionTwo = 0

        if (i % 2) == 0:
            numberOne = grid[0][i]
            operator = grid[1][i]
            numberTwo = grid[2][i]
            solutionTwo = calculate(operator, numberOne, numberTwo)

            numberOne = grid[2][i]
            operator = grid[1][i]
            numberTwo = grid[0][i]
            solutionOne = calculate(operator, numberOne, numberTwo)

            verticalSolutions.append([solutionOne, solutionTwo])


createGrid()
generateSolution(grid)
printGridWithSolutions(grid,horizontalSolutions,verticalSolutions)