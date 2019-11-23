import pygame
import time




class handle():

    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.sizeX = 90
        self.sizeY = 90
        self.minWidth = 0
        self.minHeight = 0
        self.cfWidth = 0
        self.cfHeight = 0
        self.columnWidth = 10
        self.coinsRadius = 37
        self.computeSizes()
        self.valueFont = pygame.font.Font("verdana.ttf", 50)

    def launchCore(self):
        self.window = pygame.display.set_mode((self.width, self.height))

    def setWindowSize(self, Width, Height):
        self.width = Width
        self.height = Height

    def setSize(self, Width, Height):
        self.sizeX = Width
        self.sizeY = Height

    def computeSizes(self):
        self.minWidth = (self.width - self.width*self.sizeX/100)/2
        self.minHeight = (self.height - self.height*self.sizeY/100)/2
        self.cfWidth = self.width*self.sizeX/100
        self.cfHeight = self.height * self.sizeY / 100
        self.coinsRadius = int(self.cfHeight/15)

    def drawEverything(self, coins, player):
        if player == 1:
            self.drawBackground((255, 0, 0))
        if player == 2:
            self.drawBackground((255, 255, 0))
        self.drawCF()
        self.drawCoins(coins)
        pygame.display.flip()

    def drawBackground(self, color):
        pygame.draw.rect(self.window, color, pygame.Rect((0, 0), (self.width, self.height)))

    def drawCF(self):
        pygame.draw.rect(self.window, (40, 40, 40), pygame.Rect((self.minWidth - self.columnWidth, self.minHeight - self.columnWidth),
                                                                (self.cfWidth + 2*self.columnWidth, self.cfHeight + 2*self.columnWidth)))
        for i in range(8):
            pygame.draw.rect(self.window, (0, 0, 255), pygame.Rect(
                (self.minWidth + (self.cfWidth/7)*i - self.columnWidth/2, self.minHeight),
                (self.columnWidth, self.cfHeight)))
        for i in range(7):
            pygame.draw.rect(self.window, (0, 0, 255), pygame.Rect(
                (self.minWidth, self.minHeight + (self.cfHeight/6)*i - self.columnWidth/2),
                (self.cfWidth, self.columnWidth)))
    def drawCoins(self, coins):
        for y in range(6):
            for x in range(7):
                if coins[x][y] == 1:
                    pygame.draw.circle(self.window, (255, 0, 0), (int(self.minWidth + (self.cfWidth/7)*(x+0.5)),
                                        int(self.minHeight + (self.cfHeight/6)*(y+0.5))), int(self.coinsRadius))
                if coins[x][y] == 2:
                    pygame.draw.circle(self.window, (255, 255, 0), (
                        int(self.minWidth + (self.cfWidth / 7) * (x + 0.5)), int(self.minHeight + (self.cfHeight / 6) * (y + 0.5))),
                                       self.coinsRadius)

    def drawLine(self, p1, p2):
        for y in range(self.columnWidth):
            for x in range(self.columnWidth):
                pygame.draw.line(self.window, (255, 255, 255),
                                 ((p1[0]+0.5)*(self.cfWidth/7) + self.minWidth + x - self.columnWidth/2,
                                  self.minHeight + (self.cfHeight/6)*(p1[1]+0.5) + y - self.columnWidth/2),
                                 ((p2[0] + 0.5) * (self.cfWidth / 7) + self.minWidth + x - self.columnWidth / 2,
                                 self.minHeight + (self.cfHeight / 6) * (p2[1] + 0.5) + y - self.columnWidth / 2))

    def getColumnClicked(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                return self.parseMPosColumn(pos[0])
        return -1

    def parseMPosColumn(self, x):
        x = x - self.minWidth
        cellWidth = self.cfWidth/7
        for i in range(7):
            if cellWidth*i < x < cellWidth*(i+1):
                return i
        return -1

    def displayWinner(self, winner, coins, linepoints):
        winnerStr = "undefined"
        color = (0, 0, 0)
        textColor = (240, 240, 240)
        if winner == 1:
            color = (255, 0, 0)
            winnerStr = "rouges"
        if winner == 2:
            color = (255, 255, 0)
            winnerStr = "jaunes"
            textColor = (40, 40, 40)

        self.drawBackground(color)
        self.setSize(45, 45)
        self.computeSizes()
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect((self.minWidth, self.minHeight), (self.cfWidth, self.cfHeight)))
        self.drawCF()
        self.drawCoins(coins)
        self.drawLine(linepoints[0], linepoints[1])
        rText = self.valueFont.render("Les " + winnerStr +" gagnent", True, textColor)
        textRect = rText.get_rect()
        textRect.center = (int(self.width/2), int(4*self.height/5))
        pygame.draw.rect(self.window, color, textRect)
        self.window.blit(rText, textRect)
        pygame.display.flip()
