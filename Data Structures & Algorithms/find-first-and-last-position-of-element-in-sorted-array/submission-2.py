class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index = -1
        last_index = -1
        left = 0
        right = len(nums)-1

        if len(nums) == 0:
            return [first_index, last_index]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        if nums[left] == target:
            first_index = left

        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid -1
        if nums[right] == target:
            last_index = right
        return [first_index, last_index]
