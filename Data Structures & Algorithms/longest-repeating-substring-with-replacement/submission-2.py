from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        maxFreq = 0
        for r, char in enumerate(s):
            freq[char] += 1
            maxFreq = max(maxFreq, freq[char])
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            