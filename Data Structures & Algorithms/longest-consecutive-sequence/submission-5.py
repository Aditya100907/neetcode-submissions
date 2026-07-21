class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0
        length = 0
        for num in nums:
            if (num-1) in numset:
                continue
            while num+length in numset:
                length+=1
            max_length = max(max_length, length)
            length = 0
        return max_length