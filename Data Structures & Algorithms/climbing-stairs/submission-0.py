class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [1] * (n + 1)
        for i in range(n - 2, -1, -1):
            DP[i] = DP[i+1] + DP[i+2]
        return DP[0]
