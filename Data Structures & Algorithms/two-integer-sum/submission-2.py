class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            comp = target-num
            if comp in nums_dict:
                return [nums_dict[comp], i] 
            nums_dict[num] = i

        return []
        