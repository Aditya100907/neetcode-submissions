class Solution:
    def maxArea(self, nums: List[int]) -> int:
        best = 0
        left = 0
        right = len(nums)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(nums[left], nums[right])*(right-left))
            if nums[left] <= nums[right]:
                left+=1
            else:
                right-=1
        return max_area