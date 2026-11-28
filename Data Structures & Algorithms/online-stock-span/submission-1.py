class StockSpanner:

    def __init__(self):
        self.stock = []
        self.curr = []

    def next(self, price: int) -> int:
        if len(self.curr) == 0:
            self.stock.append(price)
            self.curr.append(1)
            return 1
        rem = 0
        while len(self.stock) != 0 and price >= self.stock[len(self.stock) - 1]:
            self.stock.pop()
            rem += self.curr.pop()
            if len(self.stock) == 0:
                continue
        self.stock.append(price)
        self.curr.append(rem + 1)
        return rem + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)