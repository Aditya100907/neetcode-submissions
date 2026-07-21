from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first get freq map of elements in nums
        # naive: sorting, tuple of value key pair
        # bucket sort algorithm

        if k == 0:
            return []
        # freq map
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        # bucket sort
        bucket = [[] for _ in range (len(nums)+1)]
        for num in freq:
            bucket[freq[num]].append(num)
        
        output = []
        # backpass to retrieve top k
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output

        

        

        

