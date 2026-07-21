class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #so we would start from i = 0
        #set left pointer as i+1
        #set right pointer to len(nums)-1
        #iterate a loop till len(nums)-2 for edge case to prevent overreaching
        #we need to skip duplicates for efficiency
        #then we go through and solve the problem
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i >0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left+=1
        return result