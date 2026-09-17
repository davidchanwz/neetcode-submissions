class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        minDP = [0] * n
        maxDP = [0] * n
        for i in range(n):
            if i == 0:
                minDP[i] = nums[i]
                maxDP[i] = nums[i]
            elif nums[i] < 0:
                maxDP[i] = max(nums[i], minDP[i-1] * nums[i])
                minDP[i] = min(nums[i], maxDP[i-1] * nums[i])
            elif nums[i] > 0:
                minDP[i] = min(nums[i], minDP[i-1] * nums[i])
                maxDP[i] = max(nums[i], maxDP[i-1] * nums[i])
            else:
                maxDP[i] = 0
                minDP[i] = 0
        return max(maxDP)