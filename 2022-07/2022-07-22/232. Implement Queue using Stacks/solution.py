class MyQueue:

    def __init__(self):
        self.stack = []
        self.invert = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.invert) == 0:
            while len(self.stack) > 0:
                self.invert.append(self.stack.pop())

        return self.invert.pop()


    def peek(self) -> int:
        if len(self.invert) > 0:
            return self.invert[-1]

        return self.stack[0]


    def empty(self) -> bool:
        return len(self.invert) == 0 and len(self.stack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()