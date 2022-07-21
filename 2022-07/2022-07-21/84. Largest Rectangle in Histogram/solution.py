from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        stack = []
        max_area = 0

        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        while len(stack) > 0:
            h = heights[stack.pop()]
            w = n if len(stack) == 0 else n - stack[-1] - 1
            max_area = max(max_area, h * w)

        return max_area
