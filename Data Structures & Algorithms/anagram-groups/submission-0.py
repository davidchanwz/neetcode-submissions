from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for string in strs:
            counts = [0] * 26
            for c in string:
                counts[ord(c) - ord('a')] += 1
            hm[tuple(counts)].append(string)
        return list(hm.values())