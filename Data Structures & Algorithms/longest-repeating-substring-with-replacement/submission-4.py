from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = defaultdict(int)
        l, r = 0, 0
        m, res = 0, 0
        while r < len(s):
            tracker[s[r]] += 1

            m = max(m, tracker[s[r]])

            if (r - l + 1) - m > k:
                tracker[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
            r += 1

        return res


            
            