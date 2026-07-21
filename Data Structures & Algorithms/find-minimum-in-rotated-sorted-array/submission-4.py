class Solution:
    def findMin(self, nums: List[int]) -> int:
        # compute the mid
        # if mid is bigger than the left, bring left in
        # if mid is smaller than the left, bring right in
        # 1. original array, smallest number is first and rotations cancel out
        # 2. an array that is split  by any inflection point where to the left is ordered bigger numbers, to the right is ordered smaller numbers
        # we need to find the inflection point, and get the first number in the sequence of smaller numbers in situation 2
        # while also having it be tolerant of the edge case where its just the original array
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] <= nums[left] and nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[left] < nums[right]:
                return nums[left]
            else:
                right = mid
        return nums[left]


        