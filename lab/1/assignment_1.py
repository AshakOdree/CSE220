import random
def MusicalChair(sOurCE):
    eND = 6
    sIZe = 7
    iK=0
    #loop start
    while True:
        tEmp1 = sOurCE[eND]
        #new loop start
        coUNT=0
        j = 0
        while(coUNT<sIZe-1):
            sOurCE[eND] = sOurCE[eND-1]
            eND-=1
            #condition star
            if eND<0:
                eND = len(sOurCE)-1
            else:
                None

            coUNT+=1
        #new loop end
        sOurCE[0] = tEmp1
        eND = sIZe-1
        n = random.randint(0, 3)
    #loop end
        #condition start
        if n==1:
            sOurCE.pop(sIZe//2)
            sIZe-=1
            eND =sIZe-1
            #new condition
            if len(sOurCE)==1:
                print(sOurCE[0])
                break
            else:
                x=0
                while (x<len(sOurCE)):
                # for x in range(len(arr)):
                    print(sOurCE[x],end=" ")
                    x+=1
                print()
            #end
        else:
            None
aRRay = [1,2,3,4,5,6,7]
MusicalChair(aRRay)
