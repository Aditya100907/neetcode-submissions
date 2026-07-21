from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = defaultdict(int)
        for num in nums:
            if num in single:
                del single[num]
            else:
                single[num]+=1
        return next(iter(single))