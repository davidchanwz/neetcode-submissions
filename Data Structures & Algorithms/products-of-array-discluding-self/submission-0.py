class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                suffix[i] = nums[i+1] * suffix[i+1]
        out = [0 for _ in range(n)]
        for i in range(len(nums)):
            out[i] = prefix[i] * suffix[i]
        return out

        