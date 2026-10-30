class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(idx, need, arr):
            if need < 0:
                return
            elif need == 0:
                res.append(arr[:])
                return
            for i in range(idx, n):
                arr.append(nums[i])
                dfs(i, need-nums[i],arr)
                arr.pop()
        dfs(0, target, [])
        return res
