class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, num in enumerate(nums):
            left = i+1
            right = len(nums)-1
            if i >0 and num == nums[i-1]:
                continue
            while left < right and left < len(nums)-1 and right > i+1:
                if num + nums[left] + nums[right] == 0:
                    output.append([num, nums[left], nums[right]])
                    curr = left
                    while left+1 < len(nums)-1 and nums[left+1] == nums[curr]:
                        left+=1
                    else:
                        left+=1
                elif num + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1
        return output
            