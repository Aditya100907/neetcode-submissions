class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxl, maxr = height[left], height[right]
        total = 0
        while left < right:

            while left < right and height[left+1] >= height[left]:
                left+=1
                change = min(maxl, maxr)-height[left]
                if change > 0:
                    total+=change
                maxl = max(maxl, height[left])
            while left < right and height[right-1] >= height[right]:
                right-=1
                change = min(maxl, maxr)-height[right]
                if change > 0:
                    total+=change
                maxr = max(maxr, height[right])

            if left < right:
                if maxl <= maxr:
                    left+=1
                    total+=maxl-height[left]
                else: 
                    right-=1
                    total+=maxr-height[right]

        return total



            