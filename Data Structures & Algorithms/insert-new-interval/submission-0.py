class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        start, end = newInterval

        for s,e in intervals:
            if e<start:
                result.append([s,e])
            
            elif s>end:
                result.append([start, end])
                start, end = s, e

            else:
                start = min(start, s)
                end = max(end, e)

        result.append([start, end])

        return result