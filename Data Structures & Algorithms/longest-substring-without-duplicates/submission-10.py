class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        out = 0
        for r, char in enumerate(s):
            if char in seen:
                l = max(l, seen[char] + 1)
            seen[s[r]] = r
            out = max(out, r - l + 1)
        return out
            
