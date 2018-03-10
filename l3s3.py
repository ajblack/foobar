def findNextMultipleIndex(mylist, multIndex, currentIndex):
    #find the next index in the list that cleanly divides the passed index
    for j in range(currentIndex+1, len(mylist)):
        if mylist[j]%mylist[multIndex]==0:
            return j
    #if a multiple is not found, then return the length of the array
    return len(mylist)

def getMatches(l):
    #if the list has less than three entries then it can't have any matching tuples
    if len(l) < 3:
        return []
    listLength = len(l)
    returnList = []

    p1Index=0
    p2Index=1
    p3Index=2
    #while p1Index < len(l)-2:
    while p1Index < len(l)-2:
        while p2Index < len(l)-1:
            while p3Index < len(l):
                if l[p3Index]%l[p2Index]==0 and l[p2Index]%l[p1Index]==0:
                    p="match found with P1: %s, P2: %s, P3: %s"%(l[p1Index], l[p2Index], l[p3Index])
                    #print(p)
                    returnList.append(''+str(l[p1Index])+","+str(l[p2Index])+","+str(l[p3Index]))
                p3Index = findNextMultipleIndex(l, p2Index, p3Index)
            p2Index=findNextMultipleIndex(l, p1Index, p2Index)
            p3Index=findNextMultipleIndex(l, p2Index, p2Index)
        p1Index+=1
        p2Index=findNextMultipleIndex(l,p1Index,p1Index)
        p3Index=findNextMultipleIndex(l,p2Index,p2Index)
    return returnList




def getMultiplesOfInt(value, mylist):
    ret = []
    for i in mylist:
        if value%i==0 and i<=value:
            ret.append(i)
    return ret

def answer(l):
    tuplesSet = set()
    mydict = {}
    for v in l:
        mydict[v] = getMultiplesOfInt(v, l)
    for mykey, myvalue in mydict.items():
        if len(myvalue)>2:
            valList = getMatches(myvalue)
            for matchVal in valList:
                tuplesSet.add(matchVal)
    return len(tuplesSet)



l1 =[5,12,20,25,100,112,120,200,240]
l2 =[5,12,20,25,100,112,200]
v=answer(l1)
print(v)
c=answer(l2)
print(c)
