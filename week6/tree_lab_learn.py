class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

#             A
#         /   |   \
#     B       C       D
#   /   \             |
#  E     F            G
#      /   \        /   \
#    H       I    J       K

h = TreeNode("H")
i = TreeNode("I")
j = TreeNode("J")
k = TreeNode("K")

e = TreeNode("E")
f = TreeNode("F", [h, i])
g = TreeNode("G", [j, k])

b = TreeNode("B", [e, f])
c = TreeNode("C")
d = TreeNode("D", [g])

tree = TreeNode("A", [b, c, d])

#Defines a method (A function that belongs to TreeNode) Self is the node you call it on.
#Run tree.valuesDFS(), self is A, the top of the tree

#DFS - Preorder (Forward) Top Down, Postorder Down Up, Reverse (Right side)
#BFS - Side to side or reverse order side to side

def valuesDFS(self):
    #empty list where you write down node names
    result = []
    #the Plates, which starts with one plate, root A
    stack = [self]

    #As long as the stack isn't empty
    while stack:
        #take the top plate off (the right most)
        node = stack.pop()
        #Stick node.val at the end of Result 
        result.append(node.val)

        #Then for child in the reverse of current node's children, put the children in the stack in reverse order
        for child in reversed(node.children):
            stack.append(child)
    #When the pile is empty hand back the list of names 
    return result
