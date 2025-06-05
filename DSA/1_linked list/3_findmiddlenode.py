#find the middle node.can only loop the linked list only once.

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList():
    def __init__(self,val):
        self.head=Node(val)
        self.tail=self.head

    def insert(self,val):
        new_node=Node(val)
        self.tail.next=new_node
        self.tail=new_node

    def display(self):
        temp_node=self.head
        while(temp_node!=None):
            print(temp_node.val,end=" ")
            temp_node=temp_node.next

    def findmiddlenode(self):
        slow=self.head
        fast=self.head
        middlenode=None
        while fast:
            if fast.next:
                slow=slow.next
                fast=fast.next.next
            else:
                break
        middlenode=slow
        print(middlenode.val)
        

val=input("type value to insert :")
ll=LinkedList(val)

while(True):
    val=input("type value to insert :")
    if val=='exit':
        break
    else:
        ll.insert(val)
    
ll.display()
print('\n')
ll.findmiddlenode()