class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in wordDict and (j+1 >= n or dp[j+1]):
                    dp[i] = True
        print(dp)
        return dp[0]
                
                    