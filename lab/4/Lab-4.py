bracket_ALL=["()","[]","{}"]
b_StArT="({["
b_cLoSE=")}]"
oPeN_bRacKet_ChEcK = []
cLoSE_bRacKet_cHecK = []



class Node:
    def __init__(self, elem, next=None):
        self.value = elem
        self.next = next

class LinkStack:
    head = None
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tree = Node(data)
            tree.next = self.head
            self.head = tree
    def peek(self):
        return (self.head.value)
    def pop(self):
        val = self.head
        self.head = self.head.next
        return (val.value)

def check(self):
    coNdItIoN = False
    tEmP = 0
    for i in iNpUT:
        if i in b_StArT:
            stack.push(i)
            tEmP += 1
            oPeN_bRacKet_ChEcK.append(tEmP)
        elif i in b_cLoSE:
            tEmP += 1
            cLoSE_bRacKet_cHecK.append(tEmP)
            if stack.head != None:
                check = stack.pop()
                check3 = [i]
                c = oPeN_bRacKet_ChEcK.pop()
                if check+i not in bracket_ALL:
                    coNdItIoN = True
                    print("The expression is NOT correct")
                    print("Error at character # ", c, ".'", check, "'- not closed.")
                    break
            else:
                coNdItIoN = True
                # check3.append(i)
                problem = cLoSE_bRacKet_cHecK.pop()
                print("The expression is NOT correct")
                print("Error at character # ", problem, ".'", i, "'- not opened")
                break
        else:
            tEmP += 1
    if coNdItIoN == False:
        print("The expression is correct")

stack= LinkStack()
iNpUT = str(input("Enter the expression:"))
check(iNpUT)
