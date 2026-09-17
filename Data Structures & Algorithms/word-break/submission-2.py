class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        n = len(s)
        dp = [False] * n
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in dic and (j+1 >= n or dp[j+1]):
                    dp[i] = True
        return dp[0]
                
                    