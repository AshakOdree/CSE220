def hasHFuncTion(aRRay):

    lEngTH = len(aRRay)
    emT_liST = [0]*lEngTH
    #value=['A','E','I','O','U']
    for i in aRRay:
        ToTal_Sum = 0
        coNsoNanT = 0
        for idX in i:
            if idX>='A' and idX<='Z' and idX!='A' and idX!='E' and idX!='I' and idX!='O' and idX!='U':
                coNsoNanT+=1
            elif idX>='0' and idX<='9':
                ToTal_Sum+=int(idX)

        tEmP = (coNsoNanT*24+ToTal_Sum)%9

        if emT_liST[tEmP]==0:
            emT_liST[tEmP] = i
        else:
            while emT_liST[tEmP]!=0:
                tEmP = (tEmP+1)%lEngTH
            emT_liST[tEmP] = i
            
    return emT_liST

uSeR=['ABC124','CBA124','DEF456','GHIJ789','HGW654','ZYZ987','WEP274','OUY982','LZA111']
print(hasHFuncTion(uSeR))
