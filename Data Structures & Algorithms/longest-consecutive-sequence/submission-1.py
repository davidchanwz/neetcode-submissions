class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        res = 0
        for num in seen:
            if num - 1 not in seen:
                cur_num, cur_count = num, 1
                while cur_num + 1 in seen:
                    cur_num += 1
                    cur_count += 1
                res = max(res, cur_count)
        return res
            
