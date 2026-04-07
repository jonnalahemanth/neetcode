class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0) # sentinel to pop the all

        for i, h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i 
                max_area = max(max_area, height*width)
            stack.append(i)

        return max_area