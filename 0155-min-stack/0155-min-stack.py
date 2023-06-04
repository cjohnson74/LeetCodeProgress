class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal is None:
            self.minVal = val
        else:
            self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        if self.stack[-1] is self.minVal:
            self.stack.pop()
            if len(self.stack) != 0:
                self.minVal = min(self.stack)
            else:
                self.minVal = None
        else:
            self.stack.pop()
        print(self.stack, self.minVal)
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()