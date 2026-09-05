class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            l, r = i + 1, n - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                total = a + b + c
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    out.append([a, b, c])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
        return out            