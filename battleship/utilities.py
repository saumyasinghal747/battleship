import random

import click
from termcolor import *

from objects import ship, board


#all the super long functions ;)

def placeShip(board, shipName, size,expectedSum):
    click.clear()
    #take input abt where to to ships and randomize computer ships
    board.newShip(ship([0, 0], size, 'h', board))
    currCoord = [0, 0]
    ort  = 'h'
    warn = False
    while True:
        click.clear()
        click.echo('Place your '+shipName+":", nl=True)
        click.echo(board) #print the interface
        click.echo(colored("Use arrow keys to move the ship.\nPress f to rotate.\nPress space to confirm.","green"))
        if warn:
            click.echo(colored("Ships may not overlap.","red"))
            warn = False
        c = click.getchar() #get the input
        if c == 'h':
            click.echo('Use arrow keys to move your ship. Press f to rotate.')
        elif c == ' ':
            if len(list(set(tuple(coord) for coord in sum([s.coords for s in board.ships],[])))) == expectedSum:
                break
            else:
                #click.echo(sum([ship.coords for ship in cBoard.ships], []))
                warn = True
        elif c == 'f': #flip the ship
            if ort=='h':
                ort = 'v'
            else:
                ort = 'h'
        elif c == '\x1b[D':
            if currCoord[1]> 0:
                currCoord[1] -= 1
        elif c == '\x1b[C':
            if (currCoord[1] < (10-size) and ort=='h') or (currCoord[1] < 9 and ort=='v'):
                currCoord[1] += 1
        elif c == '\x1b[B':
            if (currCoord[0] < 9 and ort=='h') or (currCoord[0] < (10-size) and ort=='v'):
                currCoord[0] += 1
        elif c == '\x1b[A':
            if currCoord[0] > 0:
                currCoord[0] -= 1
        del board.ships[-1] #delete that ship
        board.newShip(ship(currCoord, size, ort, board)) #make a new one at currCoord
    return None

def randomizeShips(cB):
    row = random.randint(0,8)
    col = random.randint(0,9)
    ort = random.choice(['h','v'])
    if ort == 'h':
        row,col = col,row
    cB.newShip(ship([row,col],2,ort,cB))
    while len(list(set(tuple(coord) for coord in sum([s.coords for s in cB.ships], [])))) != 5:
        if len(cB.ships) == 2:
            del cB.ships[1]
        row = random.randint(0, 7)
        col = random.randint(0, 9)
        ort = random.choice(['h', 'v'])
        if ort == 'h':
            row, col = col, row
        cB.newShip(ship([row, col], 3, ort, cB))
    while len(list(set(tuple(coord) for coord in sum([s.coords for s in cB.ships], [])))) != 8:
        if len(cB.ships) == 3:
            del cB.ships[2]
        row = random.randint(0, 7)
        col = random.randint(0, 9)
        ort = random.choice(['h', 'v'])
        if ort == 'h':
            row, col = col, row
        cB.newShip(ship([row, col], 3, ort, cB))
    while len(list(set(tuple(coord) for coord in sum([s.coords for s in cB.ships], [])))) != 12:
        if len(cB.ships) == 4:
            del cB.ships[3]
        row = random.randint(0, 6)
        col = random.randint(0, 9)
        ort = random.choice(['h', 'v'])
        if ort == 'h':
            row, col = col, row
        cB.newShip(ship([row, col], 4, ort, cB))
    while len(list(set(tuple(coord) for coord in sum([s.coords for s in cB.ships], [])))) != 17:
        if len(cB.ships)==5:
            del cB.ships[4]
        row = random.randint(0, 5)
        col = random.randint(0, 9)
        ort = random.choice(['h', 'v'])
        if ort == 'h':
            row, col = col, row
        cB.newShip(ship([row, col], 5, ort, cB))

    pass

def joinBoards(b1,b2):
    total = ''
    b1 = str(b1).split('\n')
    b2 = str(b2).split('\n')
    for i in range(11):
        total += b1[i] + '   ' +  b2[i] + '\n'
    return total

def genHit(pB,cH):
    prevShot = cH[-1]
    sideShots = []
    if prevShot[0] != 0:
        r,c = (prevShot[0] - 1, prevShot[1])
        if pB.record[r][c] == None:
            sideShots.append([r,c] )
    if prevShot[0] != 10:
        r,c = (prevShot[0] + 1, prevShot[1])
        if pB.record[r][c] == None:
            sideShots.append([r,c])
    if prevShot[1] != 0:
        r,c = (prevShot[0] , prevShot[1]-1)
        if pB.record[r][c] == None:
            sideShots.append([r,c])
    if prevShot[1] != 10:
        r,c = (prevShot[0] , prevShot[1]+1)
        if pB.record[r][c] == None:
            sideShots.append([r,c])
    for shot in sideShots:  # check if we already know where to hit
        if shot[0] >= 2:
            if pB.record[shot[0] - 2][shot[1]] == True:
                row = shot[0]
                col = shot[1]
                break
        if shot[0] <= 7:
            if pB.record[shot[0] + 2][shot[1]] == True:
                row = shot[0]
                col = shot[1]
                break
        if shot[1] >= 2:
            if pB.record[shot[0] - 2][shot[1] + 2] == True:
                row = shot[0]
                col = shot[1]
                break
        if shot[1] <= 7:
            if pB.record[shot[0]][shot[1] + 2] == True:
                row = shot[0]
                col = shot[1]
                break
    else:
        if sideShots != []:
            shot = random.choice(sideShots)
            row, col = shot[0], shot[1]
            while [row, col] in cH:
                shot = random.choice(sideShots[0])
                row, col = shot[0], shot[1]
        else:
            row,col = -1,-1
    return row,col

if __name__=="__main__":
    cBoard = board(10,10)
    pBoard = board(10,10)
    print(joinBoards(pBoard,cBoard))