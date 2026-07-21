class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) +1
        f = sorted(freq.items(), key = lambda x: x[1])
        return [x[0] for x in f[-k:]]
