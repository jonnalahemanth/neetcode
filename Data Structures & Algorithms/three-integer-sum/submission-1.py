class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left<right:
                three_sum = nums[i]+nums[left]+nums[right]
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates
                    while left<right and nums[left]==nums[left-1]:
                        left += 1
                    while left<right and nums[right]==nums[right+1]:
                        right -= 1

                elif three_sum<0:
                    left += 1
                else:
                    right -= 1

        return res



        