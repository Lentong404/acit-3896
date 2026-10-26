

class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#This function never uses val, lmao
#Bug 1: current == self compares the node to itself. It never looks at val, the thing you’re searching for. You want “is this node’s value equal to the value I’m looking for?” → current.val == val

#Bug 2: the else: return False is the exact bug from your tree find. It gives up after checking only the first node. It also means current = current.next can never run, since both branches return before reaching it. “Not found” is only true once the loop has checked everything, so it goes after the loop.
    def contains(self, val):
        current = self

        while current is not None: 

            if current == self:
                return True
            else:
                return False
            current = current.next

    def contains(self, val):
        current = self
        while current is not None:
            if current.val == val:
                return True
            current = current.next
        return False                 # only after checking every node      


a = LLNode("A")
b = LLNode("B")
c = LLNode("C")

a.next = b
b.next = c

print(a.contains("A"))   # True
print(a.contains("C"))   # True
print(a.contains("X"))   # False

print(b.contains("A"))   # False
print(b.contains("C"))   # True