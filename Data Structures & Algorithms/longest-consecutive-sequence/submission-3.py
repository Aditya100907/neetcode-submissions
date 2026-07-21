class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert to a set for easy look up
        # as we check each number, need to see if thats the start of a sequence, if 
        # keep going forward seeing if next number is in set, save best length
        snums = set(nums)
        best = 0
        x = True
        for num in snums:
            if num-1 not in snums:
                length = 1
                while num+length in snums:
                    length+=1
                best = max(best, length)
        return best
