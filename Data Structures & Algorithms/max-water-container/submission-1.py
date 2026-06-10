class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L= 0
        R = len(heights) - 1
        res = 0

        while L < R:
            area = (R - L) * min(heights[L], heights[R])

            if heights[L] <= heights[R]:
                L += 1
            
            elif heights[R] <= heights[L]:
                R -= 1
            
            res = max(area, res)
        
        return res