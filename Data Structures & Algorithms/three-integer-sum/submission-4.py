class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            seen = set()
            j = i + 1
            while j < n:
                b = nums[j]
                c = -b-a
                if c in seen:
                    out.append([a, b, c])
                    while j + 1 < n and nums[j] == nums[j+1]:
                        j+=1
                seen.add(b)
                j += 1
        return out
