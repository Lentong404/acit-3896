from collections import deque

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

    def valuesDFS(self):
        result = []
        stack = [self]

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result

    def valuesBFS(self):
        result = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            for child in node.children:
                queue.append(child)

        return result

    


# Build the lab's tree (bottom up, so children exist before parents)
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

print(tree.valuesDFS())
print(tree.valuesBFS())


