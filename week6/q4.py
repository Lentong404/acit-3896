class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

    #Return a node whose value is equal to val or None if there is no matching node in the subtree starting at self. 
    def findTest(self, val):
        #Val is meant to come from whoever calls the function, i.e. print(tree.find("B")), otherwise it just searches for B
        val = "B"
        stack = [self]

        ##The current while loop checks if node is in val, and if it isn't, returns none immediately LMAO
        while stack:
            node = stack.pop()
            # Node is a WHOLE treenode object, and val is a string. So you want to ask if node.val == val (node's name equal to what I'm looking for?)
            if node in val:
                # When you find the node you want, no need to stick it in a variable, just return node
                val = node
            else:
                return None
            #The children don't get pushed into the stack after the first one is run. It gets popped, but then theres nothing LOL
        return val

    def find(self, val):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node

            for child in reversed(node.children):
                stack.append(child)

        return None

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

print(tree.find("G").val)   # .val prints the name, otherwise it prints <__main__.TreeNode object at 0x000002F4134B6AD0>
print(tree.find("Z"))       # None
print(b.find("G"))          #
