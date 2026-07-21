class Solution:
    def maxArea(self, nums: List[int]) -> int:
        best = 0
        left = 0
        right = len(nums)-1
        while left < right:
            best = max(best, min(nums[left], nums[right])*(right-left))
            if nums[left] <= nums[right]:
                left+=1
            else:
                right-=1
        return best