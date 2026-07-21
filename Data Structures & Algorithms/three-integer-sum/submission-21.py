class Solution:
    def threeSum (self, nums: List[int]) -> List[List[int]]:
        # important is no duplications
        #array would be easiest to work with if we sorted it, this would bring O(nlogn) time complexity
        # we need an O(n^2) approach
        # what if for each index 
        nums = sorted(nums)
        result = []
        used = set()
        for i in range (len(nums)-2):
            left = i+1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]]) 
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif current_sum < 0:
                    left+=1
                else:
                    right-=1
        return result
                    



            