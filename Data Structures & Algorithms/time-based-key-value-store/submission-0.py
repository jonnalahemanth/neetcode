class TimeMap:

    def __init__(self):
        self.store = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, [])
        left, right = 0, len(vals)-1
        res = ""

        while left<=right:
            mid = (left+right)//2

            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                left = mid+1
            else:
                right = mid-1

        return res
        
