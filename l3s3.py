
def answer(l):
    myset = set()
    retset = set()
    sumMatches = 0
    #for v in l:
    for v in range(0,len(l)-2):
        for innerV in range(v+1,len(l)-1):
            if l[innerV]%l[v]==0:
                myset.add((l[v],l[innerV],innerV))
    print(myset)
    print(l)
    for myV1, myV2, myV3 in myset:
        #for listVal in l[mytuple[2]+1:]:
        for listVal in range(myV3+1, len(l)):
            if  l[listVal]%myV2==0:
                sumMatches+=1
    return sumMatches

def findIndexOfNextMultiple(value, valIndex, l):
    for i in range(valIndex+1, len(l)):
        if l[i]>=value and l[i]%value ==0:
            return i
    return len(l)

def findMatchesInArray(l):
    sol =0
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if l[j]%l[i]==0:
                sol+=1
    return sol

def answer2(l):
    startDict={}
    sol = 0
    for i in range(0, len(l)):
        startDict[(l[i],i)]=[]
    print(startDict)
    for val,index in startDict.keys():
        currentHigh = 0
        for i in range(index+1, len(l)):
            if l[i]%val==0:
                startDict.get((val, index)).append(l[i])
                currentHigh = l[i]
    print(startDict)
    for key,val in startDict.items():
        if len(val)>1:
            sol+=findMatchesInArray(val)
    print(sol)
    return startDict

def numMultiples(l, index):
    myval = l[index]
    ret=0
    for i in range(index+1, len(l)):
        if l[i] % myval == 0:
            ret+=1
    return ret


def numDividers(l, index):
    myval = l[index]
    ret=0
    for i in range(0, index):
        if myval % l[i] == 0:
            ret+=1
    return ret

def answer(l):
    list_size = len(l)
    count = 0
    while list_size >= 2:
        list_size -= 1
        count += numDividers(l, list_size) * numMultiples(l, list_size)

    return count
#l1 =[5,12,20,25,100,112,120,200,240]
'''
l3 =[6,5,4,3,2,1,3,6,1,3,6]
#v=answer(l1)
#print(v)
c=answer(l3)
print(c)
'''

l3 =[6,5,4,3,2,1,3,6,1,3,6]
l4=[1,2,3,3,3,3,5,6]


c=answer(range(1,2001))
print(c)
