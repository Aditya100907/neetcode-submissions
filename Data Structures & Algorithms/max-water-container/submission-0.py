class Solution:
    def maxArea(self, nums: List[int]) -> int:
        # logic:
        # start with pointers on the outer ends, save that as best to start and keep a live track of what the best is throughout
        # always move the shorter height in. you gain nothing by moving the taller height in because the height is already capped by the shorter one, even if u get a taller height by moving the taller one in, itll still be limited and itll jut be worse because u lose width
        # keep moving the shorter height in from opposite ends while left < right
        # update best when u get a better one
        left = 0
        right = len(nums)-1
        best = 0
        while left < right:
            curr = min(nums[left], nums[right]) * (right-left)
            best = max(curr, best)
            if nums[left] < nums[right]:
                left+=1
            else:
                right-=1
        return best
