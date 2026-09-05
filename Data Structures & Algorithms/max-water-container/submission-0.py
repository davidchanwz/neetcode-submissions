class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l, r = 0, n - 1
        while l < r:
            amt = min(heights[l], heights[r]) * (r - l)
            res = max(amt, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res