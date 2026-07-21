class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            kmid = left + (right - left) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / kmid)
            if total > h:
                left = kmid+1
            elif total <= h:
                right = kmid

        return left