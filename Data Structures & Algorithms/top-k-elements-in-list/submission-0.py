class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        freq = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            freq[count-1].append(num)
        counter = 0
        res = []
        while counter < k:
            res += freq[-1]
            counter += len(freq[-1])
            freq.pop()
        return res