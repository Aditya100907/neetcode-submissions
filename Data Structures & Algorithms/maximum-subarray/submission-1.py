class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes algorithm, keep track of current keep track of best, reset current as u go
        curr = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            best = max(best, curr)
        return best