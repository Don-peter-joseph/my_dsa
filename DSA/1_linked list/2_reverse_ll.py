#reverse a linked list

class LinkedList():
    def __init__(self):
        self.head=None
        self.temp_node=None
        self.tail=None

    def insert(self,val):
        if self.head:
            new_node={'item':val,'next':None}
            self.temp_node['next']=new_node
            self.temp_node=self.tail=new_node
        else:
            node={'item':val,'next':None}
            self.temp_node=node
            self.head=node
            self.tail=node

    def display(self):
        if self.head:
            self.temp_node=self.head
            while(self.temp_node['next']!=None):
                print(self.temp_node['item'],end=" ")
                self.temp_node=self.temp_node['next']
            print(self.temp_node['item'])

    def reverse_ll(self):
        self.temp_node=self.head
        current_node=self.temp_node['next']
        while current_node['next']!=None:
            if self.temp_node==self.head:
                self.temp_node['next']=None
                next=current_node['next']
                current_node['next']=self.temp_node
                self.temp_node=current_node
                current_node=next
            else:
                next=current_node['next']
                current_node['next']=self.temp_node
                self.temp_node=current_node
                current_node=next
        current_node['next']=self.temp_node
        self.temp_node=self.head
        self.head=self.tail
        self.tail=self.temp_node

ll=LinkedList()

while(True):
    val=input('Enter value to linked list:')
    if val=='exit':
        break
    else:
        ll.insert(val)

ll.display()
ll.reverse_ll()
ll.display()