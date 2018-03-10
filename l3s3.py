def answer(l):
    myset = set()
    lset = set()
    sumMatches = 0
    outerIndex=1
    #for v in l:
    for v in range(0,len(l)-2):
        for innerV in range(outerIndex,len(l)-1):
            if l[innerV]%l[v]==0:
                myset.add((l[v],l[innerV],innerV))
        outerIndex +=1
    print(myset)

    listIndex = 0
    for listVal in l:
        for v1,v2,index in myset:
            if  listVal >= v2 and  listVal%v2==0 and listIndex>index:
                sumMatches+=1
        listIndex+=1
    return sumMatches


l1 =[5,12,20,25,100,112,120,200,240]
l2 =[5,12,20,25,100,112,200]
v=answer(l1)
print(v)
c=answer(l2)
print(c)


l3=[1,1,1]
c=answer(l3)
print(c)
