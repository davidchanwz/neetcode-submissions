class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        res = 0
        for num in seen:
            if num - 1 not in seen:
                cur = 1
                while num + 1 in seen:
                    num += 1
                    cur += 1
                res = max(res, cur)
        return res
            
