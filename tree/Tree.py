class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# making a tree with the help of priorder and inorder 
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    
    root_data = preorder.pop(0)
    root = TreeNode(root_data)
    
    
    root_index = inorder.index(root_data)
    
    
    root.left = build_tree(preorder, inorder[:root_index])
    root.right = build_tree(preorder, inorder[root_index + 1:])
    
    return root

ino = input().split(" ")
pre = input().split(" ")
tree = build_tree(pre , ino)

