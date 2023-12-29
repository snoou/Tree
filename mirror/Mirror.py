class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def mirror (root):
    if not root :
        return  
    
    mirror(root.right)
    mirror(root.left)
    
    temp = root.left
    root.left = root.right 
    root.right = temp
    
    
def inOrder(node):
 
    if (node == None):
        return
 
    inOrder(node.left)
    print(node.value, end=" ")
    inOrder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
mirror(root)
print ("\n")
inOrder(root)
 
    