from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #go through the array
        # add to a map of seen, key is the number and value is index
        # its okay if old indexes are overridden because we prefer indexes later in the array
        # because it makes the difference between i and j smaller and more likely to be less than k
        # if a number has been seen, we computer its abs(i-j) and return true if it exists
        d = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]]-i) <=k:
                    return True 
            d[nums[i]]=i
        return False
