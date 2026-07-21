class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        right_pass = 1
        left_pass = 1
        for i in range (1, len(nums)):
            right_pass *= nums[i-1]
            output[i]*=right_pass
        for j in range (len(nums)-2, -1, -1):
            left_pass *= nums[j+1]
            output[j]*=left_pass
        return output