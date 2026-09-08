from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        freq = defaultdict(int)
        minL = len(s) + 1
        need = 0
        out = ""
        for char in t:
            if char not in freq:
                need += 1
            freq[char] += 1
        for r, char in enumerate(s):
            freq[char] -= 1
            if freq[char] == 0:
                need -= 1
            while need == 0:
                if minL > r - l + 1:
                    out = s[l:r+1]
                    minL = r - l + 1
                freq[s[l]] += 1
                if freq[s[l]] > 0:
                    need += 1
                l += 1
        return out