class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST():
    def __init__(self):
        self.head=None
    def insert(self,value):
        node=Node(value)
        if not self.head:
             self.head=node
        else:
            temp=self.head
            while temp:
                # print(temp.value)
                if value<temp.value and temp.left:
                    temp=temp.left
                elif value<temp.value:
                    temp.left=node
                    break
                if value>temp.value and temp.right:
                    temp=temp.right
                elif value>temp.value:
                    temp.right=node
                    break
                if temp.value==value:
                    print("\nvalue already exists\n")
                    break

    def traverse(self,temp):
        if not temp:
            return None
        if not temp.left:
            print(temp.value)
        else:
            self.traverse(temp.left)
            print(temp.value)
        if temp.right:
            self.traverse(temp.right)

    def show(self):
        temp=self.head
        self.traverse(temp)
    
    def check(self,value,temp):
        if not temp:
            return False
        if temp.value==value:
            return True
        if value<temp.value:
            return self.check(value,temp.left)
        else:
            return self.check(value,temp.right)

    def find(self,value):
        temp=self.head
        ans=self.check(value,temp)
        print(ans)

tree=BST()

while True:
    val=int(input("Enter the value to insert :"))
    if val==-1:
        break
    tree.insert(val)

tree.show()
tree.find(7)
