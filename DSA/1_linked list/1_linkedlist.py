
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
    
    def prepend(self,value):
        node={'item':value,'next':None}
        node['next']=self.head
        self.head=node

    def append(self,value):
        node={'item':value,'next':None}
        self.tail['next']=node
        self.tail=node

    def insert_at_index(self,index,value):
        node={'item':value,'next':None}
        self.temp_node=self.head
        for i in range(index):
            if i==index-1:
                node['next']=self.temp_node['next']
                self.temp_node['next']=node
                break
            else:
                print(self.temp_node)
                self.temp_node=self.temp_node['next']

ll=LinkedList()

while(True):
    val=input('Enter value to linked list:')
    if val=='exit':
        break
    else:
        ll.insert(val)

ll.display()
ll.prepend(5)
ll.display()
ll.append(53)
ll.display()
ll.insert_at_index(4,13)
ll.display()