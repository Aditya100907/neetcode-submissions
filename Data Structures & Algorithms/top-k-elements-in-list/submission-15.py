from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        buckets = [[] for i in range(len(nums)+1)]
        for num in freq:
            buckets[freq[num]].append(num)
        
        output = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output)==k:
                    return output

        return output

