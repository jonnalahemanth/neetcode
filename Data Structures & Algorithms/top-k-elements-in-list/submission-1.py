from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        # create bucket
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in nums_dict.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) ==k:
                    return res
        return res
        
        # heap = []

        # for num, freq in nums_dict.items():
        #     heapq.heappush(heap, (freq, num))

        #     if len(heap) >k:
        #         heapq.heappop(heap)


        # return [num for _, num in heap] 

        