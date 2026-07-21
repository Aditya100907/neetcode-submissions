class Solution:
    def findMin(self, nums: List[int]) -> int:
        #only move left if we are sure that left is not min to what would be min, return left at end
        # only move left if right is less than left
        # if right is greater than left move right in
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[left]:
                if nums[mid] > nums[left]:
                    left = mid+1
                elif nums[mid] < nums[left]:
                    right = mid
                else:
                    left+=1
            else:
                return nums[left]

        return nums[left]
