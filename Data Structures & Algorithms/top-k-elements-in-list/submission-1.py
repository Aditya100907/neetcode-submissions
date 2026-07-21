class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) +1
        f = [[] for _ in range (len(nums) + 1)]
        for x in freq.items():
            f[x[1]].append(x[0])
        result = []
        for i in range(len(f) - 1, 0, -1):
            for num in f[i]:
                result.append(num)
                if len(result)==k:
                    return result
