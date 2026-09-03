class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26
        for c in s:
            chars[ord('a') - ord(c)] += 1
        for c in t:
            chars[ord('a') - ord(c)] -= 1
        for n in chars:
            if n != 0:
                return False
        return True