import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        size = 0

        for stone in stones:
            heapq.heappush(heap, -stone)
            size += 1
        
        while size and size>1:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            size -= 2
            if first!=second:
                heapq.heappush(heap, -(first-second))
                size += 1
            
        return -heap[0] if heap else 0
        