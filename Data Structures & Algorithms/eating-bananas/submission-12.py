class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink, maxk = 1, max(piles)

        while mink < maxk:
            k = mink + (maxk-mink) // 2
            hours = 0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours <= h:
                maxk = k
            else:
                mink = k+1
        return mink
