class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        while min_k < max_k:
            k = min_k + (max_k - min_k) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                max_k = k
            else:
                min_k = k+1
        
        return min_k