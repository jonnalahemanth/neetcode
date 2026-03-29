from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        heap = []

        for num, freq in nums_dict.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) >k:
                heapq.heappop(heap)


        return [num for _, num in heap] 

        