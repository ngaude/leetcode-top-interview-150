class MinStack:

    def __init__(self):
        self.l = []

    def push(self, value: int) -> None:
        if len(self.l) == 0:
            self.l.append((value,value))
        else:
            self.l.append((value,min(value,self.l[-1][1])))

    def pop(self) -> None:
        elt,_ = self.l.pop()
        return elt


    def top(self) -> int:
        elt = self.l[-1][0]
        return elt
        

    def getMin(self) -> int:
        _min = self.l[-1][1]
        return _min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2
