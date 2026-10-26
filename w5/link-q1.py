


class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    a = LLNode("A")
    b = LLNode("B")
    c = LLNode("C")

    a.next = b
    b.next = c


    def length(self):
        current = self
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    print(a.length())   # 3
    print(b.length())   # 2
    print(c.length())   # 1    