class Solution:
    def trap(self, height: List[int]) -> int:
        # area between two relative maximums minus area of bars in between added up
        #need to keep track of highest point
        max_l = 0
        max_r = 0
        l = 0
        r = len(height)-1
        total = 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                total+=max_l-height[l]
                l+=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                total+=max_r-height[r]
                r-=1
            
        return total

