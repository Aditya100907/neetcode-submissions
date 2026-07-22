class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_l, max_r = height[left], height[right]
        trapped = 0
        while left < right:
            if max_l <= max_r:
                left+=1
                max_l = max(max_l, height[left])
                trapped+= max_l-height[left]
            else:
                right-=1
                max_r = max(max_r, height[right])
                trapped+= max_r - height[right]
        return trapped
            # move the smaller height in (water is bounded by smaller height anyways) and capture water from next
            # repeat - O(n) time complexity, O(1) space - other option is two pass with O(n) space - 2 arrays tracking heighest height to its left and right
