class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(nums):
            prev2 = 0
            prev1 = 0

            for money in nums:
                curr = max(prev1, prev2+money)
                prev2 = prev1
                prev1 = curr

            return prev1
        
        if len(nums) == 1:
            return nums[0]
        
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))