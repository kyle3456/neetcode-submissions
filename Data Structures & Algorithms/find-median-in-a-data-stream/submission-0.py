class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 and len(self.left) == 0:
            heapq.heappush(self.left, -num)

        elif len(self.right) == len(self.left):
            biggest_left = self.left[0] * -1
            
            if num > biggest_left:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)

        elif len(self.right) > len(self.left):
                
            if num < self.right[0]:
                heapq.heappush(self.left, -num)

            else:
                heapq.heappush(self.right, num)
                curr = heapq.heappop(self.right)
                heapq.heappush(self.left, -curr)
        
        elif len(self.left) > len(self.right):
            biggest_left = self.left[0] * -1
            if num > biggest_left:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
                curr = heapq.heappop(self.left)
                heapq.heappush(self.right, -curr)

    def findMedian(self) -> float:
        if len(self.right) == 0 and len(self.left) == 0:
            return None

        if len(self.left) == len(self.right):
            l = self.left[0] * -1
            r = self.right[0]
            return (l + r) / 2
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return self.left[0] * -1
        
        