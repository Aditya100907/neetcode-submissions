class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = [1]*len(nums)
        for i, num in enumerate(nums):
            result[i] = prefix
            prefix*=num
        suffix = 1
        length = len(nums)
        for i in range (len(nums)-1, -1, -1):
            result[i]*=suffix
            suffix*=nums[i]
        return result