from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1

        bucket = [[] for _ in range(1000)]

        for num, freq in nums_dict.items():
            bucket[freq].append(num)
        res = []
        for i in range(999, 0, -1):
            for num in bucket[i]:
                if len(res) < k:
                    res.append(num)
                if len(res) == k:
                    return res

        return res

