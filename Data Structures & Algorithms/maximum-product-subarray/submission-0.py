class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            tempMax = max(n, n*currMax, n*currMin)
            currMin = min(n, n*currMax, n*currMin)
            currMax = tempMax
            res = max(res, currMax)
        return res

        