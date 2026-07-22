class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxl, maxr = height[left], height[right]
        total = 0
        while left < right:
            if maxl <= maxr:
                left+=1
                maxl = max(maxl, height[left])
                total+=maxl-height[left]
            else:
                right-=1
                maxr = max(maxr, height[right])
                total+=maxr-height[right]
        return total
            