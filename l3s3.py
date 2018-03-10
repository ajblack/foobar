def findNextMultipleIndex(mylist, multIndex, currentIndex):
    #find the next index in the list that cleanly divides the passed index
    for j in range(currentIndex+1, len(mylist)):
        if mylist[j]%mylist[multIndex]==0:
            return j
    #if a multiple is not found, then return the length of the array
    return len(mylist)

def answer(l):
    #if the list has less than three entries then it can't have any matching tuples
    if len(l) < 3:
        return 0
    numMatches = 0
    listLength = len(l)

    p1Index=0
    p2Index=1
    p3Index=2


    #while p1Index < len(l)-2:
    while len(l) > 0:
        print("moving P1")
        while p2Index < len(l)-1:
            while p3Index < len(l):
                if l[p3Index]%l[p2Index]==0 and l[p2Index]%l[p1Index]==0:
                    p="match found with P1: %s, P2: %s, P3: %s"%(l[p1Index], l[p2Index], l[p3Index])
                    print(p)
                    numMatches+=1
                p3Index = findNextMultipleIndex(l, p2Index, p3Index)
            p2Index=findNextMultipleIndex(l, p1Index, p2Index)
            p3Index=findNextMultipleIndex(l, p2Index, p2Index)
        #p1Index+=1
        #p2Index=findNextMultipleIndex(l, p1Index, p2Index)
        #p3Index=findNextMultipleIndex(l, p2Index, p2Index

        l.pop(0)
        p1Index=0
        p2Index=findNextMultipleIndex(l,p1Index,p1Index)
        p3Index=findNextMultipleIndex(l,p2Index,p2Index)
    return numMatches


l1 =[5,12,20,25,100,112,200]
v = answer(l1)
print(v)
