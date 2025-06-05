class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if not self.root:
            self.root=new_node
        else:
            temp=self.root
            while temp.left or temp.right:
                if temp.value==value:
                    return None
                if value>temp.value:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=new_node
                else:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=new_node
            if value>temp.value:
                temp.right=new_node
            else:
                temp.left=new_node
    
    # def display(self):
    def search(self,value):
        temp=self.root
        if self.root is None:
            return 'Not Found'
        while temp:
            if temp.value==value:
                return 'Found'
            elif temp.value>value:
                temp=temp.left
            else:
                temp=temp.right
        return 'Not found'

bst=BST()
while True:
    val=input("Enter the value :")
    if val=='exit':
        break
    val=int(val)
    bst.insert(val)
print(bst.search(9))
            