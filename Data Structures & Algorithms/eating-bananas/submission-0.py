class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = 0

        for pile in piles:
            max_k = max(max_k, pile)

        left, right = 1, max_k

        def num_hours(piles, k):
            hours = 0
            for pile in piles:
                hours += (pile+k-1)//k
            return hours

        while left<=right:
            mid = (left+right)//2
            hours = num_hours(piles, mid)
            if hours > h:
                left = mid+1
            else:
                right = mid-1

        return left


        