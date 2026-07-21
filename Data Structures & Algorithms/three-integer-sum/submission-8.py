class Solution:
    def threeSum (self, nums: List[int]) -> List[List[int]]:
        result = []
        # skip duplicates
        # two types of duplicates, outer duplicates to know not enter loops of things we've already done
        #also inner duplicates need to be skipped once one combo is found, still need to check for other combos just at different pointers
        # edge case protect: iterate through nums until len(nums-2), need space for both pointers as well
        # first pointer will always begin at i+1 and second pointer will begin at len(nums)-1, shrink accordingly to search
        nums.sort()
        for i in range(len(nums)-2):
            #set pointer locations
            left = i+1
            right = len(nums)-1
            #outer skip
            if i>0 and nums[i]==nums[i-1]:
                continue
            #start searching
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    #add to result
                    result.append([nums[i], nums[left], nums[right]])
                    #inner skip
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    #still check if theres other points of three sum in this outer loop
                    left+=1
                    right-=1
                #too big, need to reduce right
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                #too small, need to increase left
                elif nums[i] + nums[left] + nums[right] < 0:
                    left+=1
        return result

            