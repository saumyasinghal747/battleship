import click

from objects import *


def placeDestr(board):
    #take input abt where to to ships and randomize computer ships
    board.newShip(ship([0, 0], 3, 'h', board))
    currCoord = [0, 0]
    ort  = 'h'
    while True:
        click.echo('Place your destroyer', nl=True)
        print(board)
        c = click.getchar()
        click.echo()
        if c == 'h':
            click.echo('Use arrow keys to move your ship. Press f to rotate.')
        elif c == ' ':
            #cBoard.newShip(ship(currCoord, 3, ort, tmp))
            break
        elif c == 'f':
            if ort=='h':
                ort = 'v'
            else:
                ort = 'h'
        elif c == '\x1b[D':
            if currCoord[1]> 0:
                currCoord[1] -= 1
        elif c == '\x1b[C':
            if (currCoord[1] < 7 and ort=='h') or (currCoord[1] < 9 and ort=='v'):
                currCoord[1] += 1
        elif c == '\x1b[B':
            if (currCoord[0] < 9 and ort=='h') or (currCoord[0] < 7 and ort=='v'):
                currCoord[0] += 1
        elif c == '\x1b[A':
            if currCoord[0] > 0:
                currCoord[0] -= 1
        board.clear()
        click.echo('\n'*10)
        board.newShip(ship(currCoord, 3, ort, board))
    return None

def placeSub(board):
    #take input abt where to to ships and randomize computer ships
    board.newShip(ship([0, 0], 4, 'h', board))
    currCoord = [0, 0]
    ort  = 'h'

    while True:
        click.echo('Place your submarine', nl=True)
        print(board) #print the interface
        c = click.getchar() #get the input
        if c == 'h':
            click.echo('Use arrow keys to move your ship. Press f to rotate.')
        elif c == ' ':
            if len(list(set(tuple(sorted(sub)) for sub in board.ships[0].coords + board.ships[1].coords)) ) == 7:
                #cBoard.newShip(ship(currCoord, 4, ort, tmp))
                break
            else:
                click.echo("Ships may not overlap.")
        elif c == 'f': #flip the ship
            if ort=='h':
                ort = 'v'
            else:
                ort = 'h'
        elif c == '\x1b[D':
            if currCoord[1]> 0:
                currCoord[1] -= 1
        elif c == '\x1b[C':
            if (currCoord[1] < 6 and ort=='h') or (currCoord[1] < 9 and ort=='v'):
                currCoord[1] += 1
        elif c == '\x1b[B':
            if (currCoord[0] < 9 and ort=='h') or (currCoord[0] < 6 and ort=='v'):
                currCoord[0] += 1
        elif c == '\x1b[A':
            if currCoord[0] > 0:
                currCoord[0] -= 1
        del board.ships[1] #delete that ship
        board.newShip(ship(currCoord, 4, ort, board)) #make a new one at currCoord
    return None
