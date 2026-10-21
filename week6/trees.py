
#A list as a pile of plates 
#stack points to an array with first object "A"
stack = ["A"]
#Append puts a plate on top (right end of the list)
stack.append("B")
stack.append("C")
print(stack)        # ['A', 'B', 'C']

#Pop takes the top plate off and hands it to you.
x = stack.pop()
print(x)            # 'C'
print(stack)        # ['A', 'B']

stack = ["X"]
stack.append("Y")
stack.append("Z")
a = stack.pop()
#After append
#stack = ["X", "Y", "Z"]

#After .pop()
# a = Z 
#stack = ["X", "Y"]

##Teeny Tree
#A has two children, B and C. B and C have no children
#node.val is the node's name, and node.children is a list of it's kids.
# A.children is [B, C]
# B.children is [ ] 
# C.children is [ ]

result = []
stack = ["A"]

while stack:                              # keep going while the pile isn't empty
    node = stack.pop()                    # take the top plate
    result.append(node.val)               # write down its name
    for child in reversed(node.children): # put its kids on the pile
        stack.append(child)

#stack.pop() takes the top plate A 
#stack.append(child) in reverse order puts C, B into stack
stack = ["C","B"]
result = ["A"]

#stack.pop() yoinks B
stack = ["C"]
result = ["A", "B"]

