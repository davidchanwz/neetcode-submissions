class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = curMax = curMin = nums[0]

        for i in range(1,n):
            num = nums[i]
            if num < 0:
                curMax, curMin = curMin, curMax
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)
            res = max(res, curMax)
        return res
