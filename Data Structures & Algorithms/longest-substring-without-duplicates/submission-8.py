class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        n = len(s)
        out = 0
        while r < n:
            if s[r] not in seen or seen[s[r]] < l:
                seen[s[r]] = r
                out = max(out, r - l + 1)
                print(s[l:r+1])
            else:
                l = seen[s[r]] + 1
                seen[s[r]] = r
            r += 1
        return out
            
