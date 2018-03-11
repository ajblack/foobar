
def answer(l):
    myset = set()
    retset = set()
    sumMatches = 0
    outerIndex=1
    #for v in l:
    for v in range(0,len(l)-2):
        for innerV in range(outerIndex,len(l)-1):
            if l[innerV]%l[v]==0:
                myset.add((l[v],l[innerV],innerV))
        outerIndex +=1
    print(myset)
    print(l)
    for myV1, myV2, myV3 in myset:
        #for listVal in l[mytuple[2]+1:]:
        for listVal in range(myV3+1, len(l)):
            if  l[listVal]%myV2==0:
                p="listVal is %s and mytuple[1] is %s"%(l[listVal],myV2)
                print(p)
                retset.add((myV1,myV2,l[listVal]))
                sumMatches+=1
    return len(retset)


'''
def answer(l):
    #myset = set()
    mylist = []
    retlist = []
    outerIndex=1
    numMatches = 0
    #for v in l:
    for v in range(0,len(l)-2):
        for innerV in range(outerIndex,len(l)-1):
            if l[innerV]%l[v]==0:
                #myset.add((l[v],l[innerV],innerV))
                mylist.append((l[v],l[innerV],innerV))
        outerIndex +=1
    print(mylist)
    for v in range(0,len(mylist)):
        #for listVal in l[mytuple[2]+1:]:
        for listVal in range(mylist[v][2]+1, len(l)):
                #retlist.append((myV1,myV2,l[listVal]))
                if l[listVal]%mylist[v][1]==0:
                    numMatches+=1
    return numMatches
'''
l1 =[5,12,20,25,100,112,120,200,240]

l3 =[1,2,3,3,3,4,5,6]
v=answer(l1)
print(v)
c=answer(l3)
print(c)
