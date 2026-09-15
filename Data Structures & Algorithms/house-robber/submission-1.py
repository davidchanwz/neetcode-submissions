class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            tmp = rob1
            rob1 = max(rob2 + num, tmp)
            rob2 = tmp
        return max(rob1, rob2) 