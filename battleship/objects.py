# coding=utf-8
from termcolor import colored

#None means unexplored - gray
#True means red
#False means white

class ship:
    def __init__(self,firstCoord,size,orientation ,board):
        if orientation == 'h':
            self.coords = [[firstCoord[0],firstCoord[1]+i] for i in range(size)]
        elif orientation == 'v':
            self.coords = [[firstCoord[0]+i,firstCoord[1]] for i in range(size)]
        self.size = size
        self.board = board
        self.numSank = 0
        self.Sank = False

    def checkSink(self):
        total = 0
        for i in self.coords:
            if self.board.record[i[0]][i[1]] is True:
                total += 1
        self.numSank = total
        self.Sank = (self.numSank == self.size)


class board:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.record = [[None for i in range(width)] for j in range(height)]
        self.ships = []
        self.hideShips = False
        self.numSunk = 0
    def updateSunk(self):
        totalS = 0
        for s in self.ships:
            s.checkSink()
            if s.Sank:
                totalS += 1
        self.numSunk = totalS
    def __str__(self): #This is for printing the boards. Also, joinBoards uses this.
        if self.hideShips: #determine if we are hiding ships
            onC = None
        else:
            onC = "on_grey"
        cumul = colored('  0  1  2  3  4  5  6  7  8  9 \n',"cyan")#The header row
        letters = 'abcdefghij'.upper()
        rowC = 0 #keep a count of what row we are on
        for row in self.record:
            colC = 0 #keep a count of what column we are on
            cumul += colored(letters[rowC],"cyan")#add the row header
            for peg in row:
                if self.hasShip(rowC,colC): #if there's a ship there, then prepare to highlight it.
                    if self.getShip(rowC,colC).Sank:
                        locOnC = "on_grey"
                    else:
                        locOnC = onC
                else:
                    locOnC = None
                if peg is None:
                    cumul += colored(" ● ","white",locOnC) #unexplored
                elif peg is True:
                    cumul += colored(" ● ","red",locOnC) #hits
                elif peg is False:
                    cumul += colored(" ● ","grey") #misses will never have ships ;)
                colC += 1 #nxt column
            cumul += '\n' #move to next row
            rowC += 1
        return cumul

    def newShip(self,theShip):
        self.ships.append(theShip)

    def hit(self,row,column): #handling a dropped bomb
        for Ship in self.ships:
            if [row,column] in Ship.coords:
                self.record[row][column] = True
                return True
                break
        else:
            self.record[row][column] = False
            return False
    def hasShip(self,row,column): #rturns boolean
        for Ship in self.ships:
            if [row,column] in Ship.coords:
                has = True
                break
        else:
            has = False
        return has
    def getShip(self,row,column): #returns ship or False
        for Ship in self.ships:
            if [row,column] in Ship.coords:
                has = Ship
                break
        else:
            has = False
        return has
    def clear(self): #wipes the board clean
        self.record = [[None for i in range(self.w)] for j in range(self.h)]
        self.ships = []

