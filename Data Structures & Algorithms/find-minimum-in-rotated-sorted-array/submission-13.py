class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[right]:
                return nums[left]
            elif nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left+=1
        return nums[left]
