from collections import deque

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

    # Find the shallowest match
    # It should return a matching node that is as close to self as possible.

    #  It's just.. find() but using BFS because BFS checks from the beginning..............
    def findShallowest(self, val):
        queue = deque([self])

        while queue:
            node = queue.popleft()

            if node.val == val:
                return node

            for child in node.children:
                queue.append(child)

        return None


    def find(self, val):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node

            for child in reversed(node.children):
                stack.append(child)

        return None

x1 = TreeNode("X")
x2 = TreeNode("X")
x3 = TreeNode("X")

m = TreeNode("M", [x1])
n = TreeNode("N", [TreeNode("P"), x2])
test = TreeNode("R", [m, n, x3])

print(test.findShallowest("X") is x3)  
print(test.find("X") is x3)           