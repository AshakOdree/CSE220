class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
#task-1
class DoublyList:
    def __init__(self,a):
        self.head = Node(None)
        self.tAiL = self.head
        self.head.next = self.head
        self.head.prev = self.head
        nEW_coUnT= None
        nUm=0

        for i in a:
            nEW_coU= None
            nEw_NoDe = Node(i,None,None)

            if self.head is None:
                print("Array is Empty")
                return
            else:
                self.tAiL.next = nEw_NoDe
                nEw_NoDe.prev = self.tAiL
                #again
                self.tAiL = nEw_NoDe
                self.head.prev = self.tAiL
                self.tAiL.next = self.head
#task-2
    def showList(self):
        nEW_coUnT= None
        if self.head.next is None:
            print("Empty List")
            return
        else:
            nN = self.head.next
            while nN is not self.head:
                print(nN.data,end=" ")
                nN = nN.next
            print()
#task-3
    def insert(self,nEw_ELem,iNdEx=None):
        nN = self.head.next
        nEw_NoDE = Node(nEw_ELem)
        nUM=0
        nEW_coUnTt= None
        if iNdEx is None:
            nEW_coU= None
            #print(iNdEx)
            while nN is not self.head:
                #print(nN)
                if nN.data==nEw_ELem:
                    print("Key alreay exists!")
                    return
                nN = nN.next
            
            nUm2=0
            self.tAiL.next = nEw_NoDE
            nEw_NoDE.prev = self.tAiL
            self.tAiL = nEw_NoDE
            self.head.prev = self.tAiL
            self.tAiL.next = self.head
            #print(self.head)
            return self.head

#task-4
        else:
            coUnT_iNdEx = 0
            while nN is not self.head:
                #print(nN)
                if nN.data == nEw_ELem:
                    print(nN.data, "Key alreay exists!")
                    return
                coUnT_iNdEx+=1
                nN = nN.next
            coUnT_iNdEx-=1
            nEW_coUnT= None
            if iNdEx<0 or iNdEx>coUnT_iNdEx:
                print("Invalid index!")
                return
            #print(nN)
            nNm5=1
            x=self.head.next
            while x != self.head:
                nNm5 += 1
                x = x.next

            tEmP = 0
            nN = self.head.next
            while nN is not self.head:
                #print(nN)
                if iNdEx==tEmP:
                    pREV_NoDe = nN.prev
                    #print(iNdEx)
                    pREV_NoDe.next = nEw_NoDE
                    nEw_NoDE.next = nN
                    nN.prev = nEw_NoDE
                    nEw_NoDE.prev = pREV_NoDe
                tEmP+=1
                nN = nN.next
            #print(nN)
            #return nN

#task-5
    def count(self):
        coUnT = 1
        point = self.head.next
        while point != self.head:
            coUnT += 1
            point = point.next
        #print(coUnt)
        return coUnT

    def remove(self,index):
        idx_length = self.count()
        if index<0 or index>idx_length:
            print("Invalid Index!")
            return
        tEmP = 0
        nN = self.head.next
        while nN is not self.head:
            nEW_coUnT= None
            #print(nN)
            if tEmP==index:
                pREV_NoDe = nN.prev
                postNode = nN.next
                pREV_NoDe.next = postNode
                postNode.prev = pREV_NoDe
                return self.head
            tEmP+=1
            nN = nN.next
        #print(nN)

#task-6
    def removeKey(self,deletekey):
        nEW_coUnT= None
        nN = self.head.next
        coUnT_nEw = 1
        nUm5= 0
        while nN is not self.head:
            nUN5=0
            #print(nN)
            if nN.data==deletekey:
                pREV_NoDe = nN.prev
                postNode = nN.next
                pREV_NoDe.next = postNode
                postNode.prev = pREV_NoDe
                coUnT_nEw = 0
            nN = nN.next

        x=self.head.next
        while x !=self.head:
            nUm5 += 1
            x=x.next
        if coUnT_nEw==1:
            print("Key not found!")
            return
        else:
            return deletekey


#--------------------class call-------------------------------
lIsT = [11,12,13,14,15]
odree = DoublyList(lIsT)
print()
print("==========Task-1,2=============")
odree.showList()
print()
print("==========Task-3=============")
odree.insert(6)
odree.showList()
print()
print("==========Task-4=============")
odree.insert(100,5)
odree.showList()
print()
print("==========Task-5=============")
odree.remove(6)
odree.showList()
print()
print("===========Task-6============")
odree.removeKey(100)
odree.showList()
