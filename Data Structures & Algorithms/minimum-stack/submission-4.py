class MinStack:

    def __init__(self):
        self.m = []
        self.l = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.m) ==0 or val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        curr = self.l.pop()
        if self.m[-1] == curr:
            self.m.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.m[-1]
