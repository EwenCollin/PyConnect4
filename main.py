import display
import control



Display = display.handle()

def winCheck(coins):
    player = 0
    for y in range(6):
        for x in range(7):
            player = coins[x][y]
            if player != 0:
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and coins[x + xc][y] == player:
                    xc += 1
                    align += 1
                if align >= 4:
                    return player
                align = 0
                xc = 0
                yc = 0
                while y + yc < 6 and coins[x][y + yc] == player:
                    yc += 1
                    align += 1
                if align >= 4:
                    return player
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and y + yc < 6 and coins[x + xc][y + yc] == player:
                    xc += 1
                    yc += 1
                    align += 1
                if align >= 4:
                    return player
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and y - yc >= 0 and coins[x + xc][y - yc] == player:
                    xc += 1
                    yc += 1
                    align += 1
                if align >= 4:
                    return player
    return 0


def winLine(coins):
    player = 0
    points = []
    for y in range(6):
        for x in range(7):
            player = coins[x][y]
            if player != 0:
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and coins[x + xc][y] == player:
                    xc += 1
                    align += 1
                if align >= 4:
                    p1 = (x, y)
                    p2 = (x + xc - 1, y)
                    points.append(p1)
                    points.append(p2)
                    return points
                align = 0
                xc = 0
                yc = 0
                while y + yc < 6 and coins[x][y + yc] == player:
                    yc += 1
                    align += 1
                if align >= 4:
                    p1 = (x, y)
                    p2 = (x, y + yc - 1)
                    points.append(p1)
                    points.append(p2)
                    return points
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and y + yc < 6 and coins[x + xc][y + yc] == player:
                    xc += 1
                    yc += 1
                    align += 1
                if align >= 4:
                    p1 = (x, y)
                    p2 = (x + xc - 1, y + yc - 1)
                    points.append(p1)
                    points.append(p2)
                    return points
                align = 0
                xc = 0
                yc = 0
                while x + xc < 7 and y - yc >= 0 and coins[x + xc][y - yc] == player:
                    xc += 1
                    yc += 1
                    align += 1
                if align >= 4:
                    p1 = (x, y)
                    p2 = (x + xc - 1, y - yc + 1)
                    points.append(p1)
                    points.append(p2)
                    return points
    return 0







def addCoin(coins, x, type):
    newY = -2
    for y in range(6):
        if coins[x][y] != 0 and newY == -2:
            newY = y - 1

    if coins[x][5] == 0:
        newY = 5
    if newY >= 0:
        coins[x][newY] = type
    return coins

def isColumnNotFull(Coins, x):
    if Coins[x][0] == 0:
        return True
    else:
        return False




def createList():
    coins = []
    for y in range(7):
        coinsX = []
        for x in range(6):
            coinsX.append(0)
        coins.append(coinsX)
    return coins

def createListFilled():
    coins = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    return coins

Coins = createList()

Player = 1

Display.launchCore()
Display.computeSizes()


done = False

while not done:


    done = control.refreshEscape()
    Display.drawEverything(Coins, Player)
    column = Display.getColumnClicked()
    if isColumnNotFull(Coins, column) and 0 <= column <= 7:
        Coins = addCoin(Coins, column, Player)
        if Player == 1:
            Player = 2
        else:
            Player = 1
    if winCheck(Coins) != 0:
        Display.displayWinner(winCheck(Coins), Coins, winLine(Coins))
        Coins = createList()
        Display.setSize(90, 90)
        Display.computeSizes()
        control.waitClick()


