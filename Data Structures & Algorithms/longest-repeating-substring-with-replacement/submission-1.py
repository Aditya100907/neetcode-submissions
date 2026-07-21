from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = defaultdict(int) # freq map of chars in current window
        best = 0 # best length
        left = 0 # pointer to left
        for i in range(len(s)): # keep moving right and updating best, until invalid, then moe left
            curr[s[i]] += 1
            # max(list(curr.values()))
            while i - left + 1 > max(list(curr.values())) + k:
                curr[s[left]] -=1
                if curr[left] == 0:
                    del curr[left]
                left+=1
            best = max(best, i - left + 1)
        return best