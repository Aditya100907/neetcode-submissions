class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map
        # bucket sort 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            bucket[freq[num]].append(num)
        result = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                if len(result) < k:
                    result.append(num)
        return result