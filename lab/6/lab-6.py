#------------------------------Task-2---------------------------------------
def fiRsT(nUM,fST_IdX):
    if(fST_IdX==0):
        return nUM

    if (nUM[fST_IdX]<nUM[fST_IdX-1]):
        nUM[fST_IdX] ,nUM[fST_IdX-1] = nUM[fST_IdX-1], nUM[fST_IdX]
    else:
        pass

    return fiRsT(nUM,fST_IdX-1)
def eXtRa(self):
        nN = len(self)
        coUntER = 0
        while nN is not None:
            nN = nN.next
            coUntER+=1
        return coUntER

def inserTion_sorT(nUm,fST_IdX):
    if(fST_IdX==len(nUm)):
        return nUm

    nUm = fiRsT(nUm,fST_IdX)

    return inserTion_sorT(nUm,fST_IdX+1)

aRRaY = [10,9,8,50,6,5,4,3,2,1,588,65,111,30]
print(inserTion_sorT(aRRaY,0))
#print(shiftInsert(arr,0))
#print(eXtRa(arr,0))
print()