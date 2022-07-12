class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n

class LinkedList:

#Task-2.1 constractor
    def __init__(self, a):
        self.head = None #instance variable self.next.next.elem
        #write your code here
        tAiL = None
        for i in a:
            n= Node(i, None)
            if (self.head is None):
                self.head =n
                tAiL = n
            else:
                tAiL.next =n
                tAiL = n
#Task 2.2   showList
    def showList(self):
        #write your code here
        xZZ=0
        tEmPPp= None
        nN = self.head
        if nN is None:
            print("Empty list")
        while nN is not None:
            tEmPPp= None
            if nN.next != None:
                print(nN.elem, end = "->")
                nN = nN.next
            else:
                print(nN.elem)
                nN = nN.next
        #pass
#Task end

    #Task 2.3 Empty
    def isEmpty(self):
        #write your code here
        if self.head == None:
            return True
        else:
            return False
#Task end

    #Task-2.4 clear
    def clear(self):
        #write your code here
        self.head = None
        
#Task end
    
    #Task-2.5 and 2.6 insert
    def insert(self, newElement, index = None):
        #write your code here
        xZZ=0
        nODE=Node(newElement,None)
        nN=self.head
        if index == None:
            coNdItIoN=False
            cOuNt=0
            yE= 0
            new_nN=self.head
            while new_nN is not None:
                if new_nN.elem==newElement:
                    coNdItIoN=True
                cOuNt+=1
                new_nN=new_nN.next
            if coNdItIoN==True:
                print("key", newElement, 'key already exists')
            else:
                while nN.next is not None:
                    nN=nN.next
                nN.next=nODE
            tEmPPp= None
        elif index!= None:
            if nN==None:
                print('Empty list')
            else:
                coNdItIoN=False
                cOuNt=0 
                new_nN=self.head
                while new_nN is not None:
                    tEmPPp2= None
                    yZZZ= 0
                    if new_nN.elem==newElement:
                        coNdItIoN=True
                    cOuNt+=1
                    new_nN=new_nN.next
                if coNdItIoN==True:
                    print("key", newElement, 'already exists')
                else:
                    if index>=0 and index<=cOuNt:
                        tEmPPp3= None
                        if index==0:
                                self.head=nODE
                                nODE.next=nN
                        else:
                            tEmP=None
                            tEmP1=None
                            for jJ in range(int(index)):
                                tEmP=nN
                                tEmP1=nN.next
                                nN=nN.next
                            tEmP.next=nODE
                            nODE.next=tEmP1
        
        #return None
        
#Task end

    #task2.7 remove
    def remove(self, deleteKey):
        #write your code here
        xZZ =0
        nN = self.head
        tEmPPp11= None
        if nN == None:
            print('Empty list')
        else:
            tEmPPp3= None
            if nN.elem == deleteKey:
                self.head = nN.next
                return
            else:
                while nN.next is not None:
                    tEmPPp= None
                    if nN.next.elem == deleteKey:
                        break
                    nN = nN.next
                if nN.next is None:
                    print("Key", deleteKey, "does not exists")
                else:
                    nN.next = nN.next.next
        
        
        #return None
#Task end

    #Task-2.8 -- EvenList
    def evenList(self):
        #write your code here
        xZZ =0
        nN = self.head
        nEW_HeAD = None
        tAiL = None
        if nN==None:
            return
        while nN != None:
            tEmPPp= None
            if nN.elem % 2 == 0:
                nEW_NoDE = Node(nN.elem, None)
                if nEW_HeAD ==None:
                    tEmPPp33= None
                    nEW_HeAD = nEW_NoDE
                    tAiL = nEW_NoDE
                else:
                    tAiL.next = nEW_NoDE
                    tAiL = nEW_NoDE
            nN = nN.next
        tEmP = nEW_HeAD
        while tEmP is not None:
            yZZ= 0
            tEmPPp1= None
            if tEmP.next != None:
                print(tEmP.elem, end="-> ")
                tEmP = tEmP.next
            else:
                print(tEmP.elem)
                tEmP = tEmP.next
            
        
        #return None
#Task end

    #Task-2.9 -- Find
    def find(self, element):
        #write your code here
        tEmPPp3= None
        xZZ= 0
        nN = self.head
        while nN is not None:
            tEmPPp= None
            if nN.elem==element:
                return True
            nN = nN.next
        return False
        #return False
#task end
   
    #Task-2.10 -- Reverse List
    def reverseList(self):
        #write your code here
        xZZ =0
        tEmPPp3= None
        nEw_HeAd = None
        nN = self.head
        while nN is not None:
            tEmPPp3= None
            yZZ= 0
            nExT_NoDe = nN.next
            nN.next = nEw_HeAd
            nEw_HeAd = nN
            nN = nExT_NoDe
        self.head = nEw_HeAd
        #pass
#Task end

    #task 2.11 sort
    def sort(self):
        #write your code here
        tEmPPp3= None
        xZ = 0
        nN = self.head
        nEW_hEaD =self.head
        if nN !=None:
            while nN is not None:
                tEmPPp= None
                n2 = nN.next
                while n2 != None:
                    tEmPPp2= None
                    yZ=0
                    if n2.elem<nN.elem:
                        temp = n2.elem
                        n2.elem = nN.elem
                        nN.elem = temp
                    n2 = n2.next
                    nEW_hEaD=self.head.next
                nN = nN.next
            return self.head
        #pass
#Task end

    #task 2.12 sum
    def sum(self):
        #write your code here
        xZ= 0
        tEmPPp3= None
        nN=self.head
        cOuNt =0
        while nN is not None:
            tEmPPp= None
            cOuNt +=nN.elem
            nN=nN.next
        return cOuNt
        #return -1
#Task end
   
    #Task 2.13 rotateKTimes
    def rotateKTimes(self, k, direction):
        #write your code here
        pass
#Task end


#==========================Tester Code==========================#
        
#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = LinkedList(a)
l1.showList() #Should print: 10->20->30->40->50->60

#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = LinkedList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true

#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List

#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = LinkedList(c)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
l3.insert(100)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.insert(50) #Should print: Key 50 already exists

#Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110) 
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120) #Should print: Key 120 does not exist

#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = LinkedList(d)
l5 = l4.evenList()
#l5.showList() #Should print: 2->8

#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
found = l4.find(5)
print(found) #Should print: true
found = l4.find(4)
print(found) #Should print: false

#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList() #Should print: 1->2->5->3->8
l4.reverseList()
print("After Reverse: ", end='')
l4.showList() #Should print: 8->3->5->2->1

#Task-2.11 -- Sort
print("\n//=======Task 2.11 -- Sort =======//")
print("Before Sort: ", end='')
l4.showList() #Should print: 8->3->5->2->1
l4.sort()
print("After Sort: ", end='')
l4.showList() #Should print: 1->2->3->5->8

#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l4.showList() #Should print: 1->2->3->5->8
total = l4.sum()
print("Sum of Elements:", total)

#Task-2.13 -- Rotate
print("\n//=======Task 2.13 -- Rotate =======//")
l4.showList() #Should print: 1->2->3->5->8
l4.rotateKTimes(2, "left")
l4.showList() #Should print: 3->5->8->1->2
l4.rotateKTimes(2, "right")
l4.showList() #Should print: 1->2->3->5->8