class TimeMap:

    def __init__(self):
        self.a = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.a[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.a[key]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right < 0:
            return ""
        return arr[right][1]

