class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
class Mylist:
    def remove(self,deletekey):
        current = self.head
        prev_node = None
        while (current != None):
            if current.element == deletekey:
                prev_node.next = current.next
            else:
                prev_node = current
                current = current.next




print("\n//=======Task 2.7 -- Remove=======//")
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110) 
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120) #Should print: Key 120 does not exist