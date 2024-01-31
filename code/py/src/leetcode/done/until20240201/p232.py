class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if 0 == len(self.stack2):
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)

    def peek(self) -> int:
        if 0 == len(self.stack2):
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2[-1]

    def empty(self) -> bool:
        return 0 == len(self.stack1) and 0 == len(self.stack2)
