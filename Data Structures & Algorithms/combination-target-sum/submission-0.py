class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, need, arr):
            if need < 0:
                return
            if need == 0:
                res.append(arr[:])
                return
            else:
                for j in range(i, len(nums)):
                    num = nums[j]
                    arr.append(num)
                    helper(j, need-num, arr)
                    arr.pop()
        helper(0, target, [])
        return res

