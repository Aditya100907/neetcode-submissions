class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0]*len(height)
        maxr = [0]*len(height)
        total = 0
        for i in range(1, len(height)):
            maxl[i] = max(maxl[i-1], height[i-1])
        for i in range (len(height)-2, -1, -1)   :
            maxr[i] = max(maxr[i+1], height[i+1])

        for i, h in enumerate(height):
            if min(maxl[i], maxr[i])-h > 0:
                total+=min(maxl[i], maxr[i])-h

        return total
            