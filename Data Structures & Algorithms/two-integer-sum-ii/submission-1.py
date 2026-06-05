class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        nums_dict = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement]+1, i+1]
            nums_dict[num] = i

        return []
        