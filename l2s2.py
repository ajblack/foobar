
class Soldier:
    def __init__(self, i, d,o):
        self.index=i
        self.direction=d
        self.handshakes=0
        self.otherSoldierIndexes=o

    def checkNumHandShakes(self):
        for i in range(self.index, len(self.otherSoldierIndexes)):
            if self.direction+self.otherSoldierIndexes[i] == 0 and self.direction ==1:
                self.handshakes += 2

    def toString(self):
        p = "Soldier with index: %s, direction: %s" % (self.index,self.direction)
        print(p)


def convertStringToList(s):
    charList = list(s)
    newList = []
    for char in charList:
        if char=='-':
            newList.append(0)
        if char=='>':
            newList.append(1)
        if char=='<':
            newList.append(-1)
    return newList



s = "<<>><"
intList = convertStringToList(s)
soldiers = []
currentIndex = 0
totalHandShakes = 0
for char in intList:
    if char == 1 or char == -1:
        soldiers.append(Soldier(currentIndex, char, intList))
    currentIndex = currentIndex + 1
for s in soldiers:
    s.toString()
    s.checkNumHandShakes()
    totalHandShakes += s.handshakes

print(totalHandShakes)
