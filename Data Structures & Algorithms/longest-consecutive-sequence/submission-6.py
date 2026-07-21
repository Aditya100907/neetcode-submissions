class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        l = 0
        max_l = 0
        for num in nums:
            if (num-1) in numset:
                continue
            while (num+l) in numset:
                l+=1
            max_l = max(max_l, l)
            l = 0
        return max_l