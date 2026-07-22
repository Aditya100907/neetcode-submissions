from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        res = ""
        left, right = 0, len(pairs)-1
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
         

