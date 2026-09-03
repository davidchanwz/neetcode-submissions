class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        for i in range(1, n):
            out[i] = nums[i-1] * out[i-1]
        suffix = 1
        for i in range(n-1,-1,-1):
            out[i] *= suffix
            suffix *= nums[i]
        return out
        