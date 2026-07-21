class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need to create a frequency map of all the nums
        #need to bucket sort the values, frequency as index
        # need to iterate backwards through the bucket sorted array to get the k most frequent values
        freq = {}
        output = []
        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
        bucket = [[] for _ in range (len(nums) + 1)]
        for num in freq:
            bucket[freq[num]].append(num)
        for i in range (len(bucket)-1, -1, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output
