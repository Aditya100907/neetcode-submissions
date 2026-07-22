class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        f_area = 0
        while left < right:
            area = min(heights[left], heights[right])*(right-left)
            f_area = max(area, f_area)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        return f_area