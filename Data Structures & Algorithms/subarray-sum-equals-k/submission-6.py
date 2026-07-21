from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        prefix = 0
        total = 0
        for num in nums:
            prefix+=num
            if prefix == k:
                total+=1
            if prefix - k in d:
                total+=d[prefix-k]
            d[prefix]+=1
        return total

 
            

            