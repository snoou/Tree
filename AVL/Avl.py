class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def level (father):
    if not father:
        return 0 
    
    left_ch = level (father.left)
    right_ch = level(father.right)
    
    if left_ch < right_ch:
        return right_ch+1
    else:
        return left_ch+1

def avl (root):
    if not root :
        return True
    
    avl_left = level (root.left)
    avl_right = level(root.right)
    
    if (avl_right - avl_left) in (0 , 1 , -1) and avl(root.left) and avl (root.right):
        return True
    return False 
    
root = TreeNode(10)
root.left = TreeNode(10)
# root.right = TreeNode(10)
root.left.left = TreeNode(10)
root.left.right = TreeNode(10)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(10)

print (avl(root))

