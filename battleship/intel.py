class player:
    def __init__(self):
        self.remShips = [2,3,3,4,5] #the remaining ships to find
        self.mode = "hunt" #by default in hunt, other option is to be in "target" mode
        self.lastHit = None
        self.targets = []#when we have a hit, fill this with all surrounding.
    def chooseHit(self):
        #if the working hit is not false, then we need to check all the cells around it.
        #we should keep track of what did not work and what worked.
        #Within 4 turns, we will know the direction. (and if that was the destroyer, then set sCS to true. Move on.)
        #Once we know the direction, then we have OPTIONS.
        pass
    def getDir(self,c1,c2):
        #works
        if c1[0]==c2[0] and abs(c1[1]-c2[1])==1:#mak sure they are adjacent
            return 'h'
        elif c1[1]==c2[1] and abs(c1[0]-c2[0])==1:
            return 'v'
        else:
            return False
    def getAdj(self,coord):
        #works
        targets = []
        if coord[0] != 0:
            r, c = (coord[0] - 1, coord[1])
            targets.append([r, c])
        if coord[0] != 10:
            r, c = (coord[0] + 1, coord[1])
            targets.append([r, c])
        if coord[1] != 0:
            r, c = (coord[0], coord[1] - 1)
            targets.append([r, c])
        if coord[1] != 10:
            r, c = (coord[0], coord[1] + 1)
            targets.append([r, c])
        return targets

if __name__=="__main__":
    comp = player()
    print(comp.getDir([2,0],[0,0]))
    print(comp.getAdj([1,1]))