class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

    # def valuesDFS(self):
    #     result = []
    #     stack = [self]

    #     while stack:
    #         node = stack.pop()
    #         result.append(node.val)

    #         for child in reversed(node.children):
    #             stack.append(child)

    #     return result

##Write a method (a function inside the TreeNode Class (like valuesDFS))
    def countLeaves(self):
        count = 0
        stack = [self]

        while stack:
            node = stack.pop()

            if not node.children:  #if len(node.children) == 0: works too
                count += 1
        
            for child in reversed(node.children):
                stack.append(child)
        return count

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

print(tree.countLeaves()) #6
print(b.countLeaves()) #3
print(d.countLeaves()) #2
print(c.countLeaves()) #1