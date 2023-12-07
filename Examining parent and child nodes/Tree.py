class Node:
    def __init__(self , value) -> None:
        self.value = value 
        self.left = None
        self.right = None
    
def binary_tree (root):
    if not root or (not root.left and not root.right ):
        return True
    
    sum = 0 
    if root.left :
        sum+= root.left.value
    if root.right :
        sum+=root.right.value

    return (sum == root.value) and (binary_tree(root.left) and binary_tree(root.right))
        
    
root = Node(20)
root.left = Node(10)
root.right = Node(10)
root.left.left = Node(5)
root.left.right = Node(5)

print (binary_tree(root))

            