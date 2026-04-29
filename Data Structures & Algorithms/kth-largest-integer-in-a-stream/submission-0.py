import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap =[]
        self.size = 0
        for num in nums:
            heapq.heappush(self.heap, num)
            self.size += 1
            if self.size>k:
                heapq.heappop(self.heap)
                self.size -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.size += 1

        if self.size<self.k:
            return None
        elif self.size>self.k:
            heapq.heappop(self.heap)
            self.size -= 1

        return self.heap[0]

        
