class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right-=1
        
        new_r, r = left-1, len(nums)-1
        new_l, l = left, 0
        while l <= new_r:
            mid = l + (new_r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                new_r = mid-1
            elif nums[mid] < target:
                l = mid+1
        while new_l <= r:
            mid = new_l + (r - new_l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                new_l = mid+1

        return -1