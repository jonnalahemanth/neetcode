from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1

        heap = []
        for key, value in nums_map.items():
            heapq.heappush(heap, (-value, key))

        res = []

        for _ in range(min(k, len(heap))):
            res.append(heapq.heappop(heap)[1])
        
        return res


        