class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # if left half is sorted
            # if right half is sorted
            # one of them has to be sorted as theres only one inflection point
            if nums[mid] == target:
                return mid
            # left is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return -1
                
        return -1