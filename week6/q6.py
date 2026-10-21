from collections import deque

##Depth lives in (node, depth) pairs on the queue so the node itself never needs to store it. 
## TreeNode("H") will crash because it's missing depth argument 
## TreeNode("F", [h, i]) puts the list [h, i] into depth instead of children.

##Sneakier Reason: Depth is relative to self. B is depth 1 when you start at A but depth 0 when you call b.valuesAtDepth(...) So one fixed number on the node can't be right for both
# class TreeNode:
#     def __init__(self, val, depth, children=None):
#         self.val = val
#         self.children = [] if children is None else children
#         self.depth = depth

class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children
       

#It should return a list containing the values of all nodes at exactly target_depth, relative to self.
## Input a depth, returns the values of ALL nodes (Depth: Length of Path to the Root)

#The node self is at depth 0.

#Return the values in forward order.

#You will need to do something a little trickier than a simple traversal. One option is to put more than one value at a time on the worklist, for example (node, depth).
## Like, instead of calling JUST node = blah blah 

#BFS (Forward aka from the first node then it's neighbour)
    def valuesAtDepth(self, target_depth):
        result = []
        queue = deque([(self, 0)])          # start: (self, depth 0)

        while queue:
            node, depth = queue.popleft()   # unpack the pair

            # result.append((child, depth)) only takes one thing, so two crashes out. Also, we only want the values ["B","C","D"]
            # 
            if depth == target_depth:
                result.append(node.val)
                # result.append(node, depth)

            # (child, depth) → (child, depth + 1) A child is one level deeper than it's parent with plain depth, every node gets depth 0
            # Values at Depth 0 would return the whole tree
            for child in node.children:
                queue.append((child, depth + 1))
                # queue.append((child, depth))
        return result

#DFS Pre-order (Forward, aka from the root node, then through the last child)
    def valuesAtDepthDFS(self, target_depth):
        result = []
        stack = [(self, 0)]
        
        while stack:
            node, depth = stack.pop()

            if depth == target_depth:
                result.append(node.val)

            for child in reversed(node.children):
                stack.append((child, depth + 1))

        return result


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

#This needs to be in print(...) tree.valuesAtDepth(1) on it's own computes the answer and tosses it out so nothing shows up :sob:
# tree.valuesAtDepth(1)

print(tree.valuesAtDepth(1))