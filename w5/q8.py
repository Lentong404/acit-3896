def __init__(self, val):
    self.val = val
    self.next = None

    def find(self, val):
        current = self
        while current is not None:
            if current.val == val:
                return current
            
            current = current.next
        return None                