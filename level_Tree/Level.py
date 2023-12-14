class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level (root ):
    if not root :
        return 0 
    
    left_ch = level (root.left)
    right_ch = level(root.right)
    
    if left_ch < right_ch:
        return right_ch+1
    else:
        return left_ch+1