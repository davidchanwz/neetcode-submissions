from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        res = 0
        maxFreq = 0
        for r, char in enumerate(s):
            idx = ord(char) - ord('A')
            freq[idx] += 1
            maxFreq = max(maxFreq, freq[idx])
            while (r - l + 1) - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            