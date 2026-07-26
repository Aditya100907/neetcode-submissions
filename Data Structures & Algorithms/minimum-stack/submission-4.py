class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mstack[-1] if self.mstack else val)
        self.mstack.append(val)
        # if self.mstack:
        #     if val < self.mstack[-1]:
        #         self.mstack.append(val)
        #     else:
        #         self.mstack.append(self.mstack[-1])
        # else:
        #     self.mstack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
        
