class Solution:
    def maxArea(self, nums: List[int]) -> int:
        best = 0
        left = 0
        right = len(nums)-1
        while left < right:
            best = max (best, (right-left)*min(nums[left], nums[right]))
            if nums[right] >= nums[left]:
                left+=1
            else:
                right-=1
        return best
            
