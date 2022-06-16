"""Create a binary tree"""

class BST:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def height_of_tree(self):
        if self:
            return 0
        return 1 + max(self.height_of_tree(self.left),self.height_of_tree(self.right))

    def size_of_tree(self):
        if self:
            return 0
        return 1 + max(self.height_of_tree(self.left),self.height_of_tree(self.right))

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)


    
def tuple_to_tree(tup):
    if isinstance(tup,list) and len(tup)==3:
        node = BST(tup[1])
        node.left = tuple_to_tree(tup[0])
        node.right = tuple_to_tree(tup[2])
    elif tup is None:
        node = None
    else:
        node = BST(tup)
    return node

def tree_to_tuple(node):
    if node.left is None and node.right is None:
        return node.key
    return (tree_to_tuple(node.left), node, tree_to_tuple(node.right.key)) 

node = tuple_to_tree([[1,3,None], 2, [[None, 3, 4], 5, [6, 7, 8]]])
print(node.key)

tup = tree_to_tuple(node)

print(tup)


        
        



