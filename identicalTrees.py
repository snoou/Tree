class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def identicalTrees (root1 , root2 ):
    if not root1 and not root2 :
        return True 
    
    if (root1.value == root2.value ) and (identicalTrees(root1.left , root2.left )) and (identicalTrees (root1.right , root2.right)):
        return True 
    return False 


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print (identicalTrees(root1 , root2))