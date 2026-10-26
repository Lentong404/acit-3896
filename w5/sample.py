def __init__(self, val):
    self.val = val
    self.next = None

    def contains(self, val):
        current = self                  # start at this node
        
        while current is not None:      # until we fall off the end
            # ...do something with current...
            current = current.next      # step to the next node

# A -> B -> C -> None


# Trees	Linked          lists
# stack = [self]     ->	current = self
# while stack:       ->	while current is not None:
# node = stack.pop() ->	(just use current)
# push all children	 -> current = current.next