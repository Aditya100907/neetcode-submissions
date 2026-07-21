class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            left = i+1
            right = len(nums)-1
            if i > 0 and num == nums[i-1]:
                continue
            while left < right:
                if num + nums[left] + nums[right] == 0:
                    output.append([num, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                elif num + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left+=1
        return output
