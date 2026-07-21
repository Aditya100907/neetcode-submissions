class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxl, maxr = height[left], height[right]
        total = 0
        while left < right:
            while left < right and height[left+1] >= height[left]:
                if min(maxl, maxr)-height[left+1] >0:
                    total+=min(maxl, maxr)-height[left+1]
                left+=1
                maxl = max(maxl, height[left])
            while left < right and height[right-1] >= height[right]:
                if min(maxl, maxr)-height[right-1] >0:
                    total+=min(maxl, maxr)-height[right-1]
                right-=1
                maxr = max(maxr, height[right])
            if left < right and maxl <= maxr:
                total+=maxl-height[left+1]
                left+=1
            elif left < right and maxr<maxl:
                total+=maxr-height[right-1]
                right-=1
        return total



            