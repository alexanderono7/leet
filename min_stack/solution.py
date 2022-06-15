class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(stack)-1]

    def getMin(self) -> int:        
        return min(self.stack)

obj = MinStack()
obj.push(3)
#obj.pop()
