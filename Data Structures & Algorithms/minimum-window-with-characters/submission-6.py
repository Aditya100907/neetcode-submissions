from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        key = defaultdict(int)
        for char in t:
            key[char]+=1
        left_best = 0
        right_best = float('inf')

        l = 0
        curr = defaultdict(int)
        have = 0

        total = len(key)

        for r in range(len(s)):
            curr[s[r]]+=1
            if curr[s[r]] == key[s[r]]:
                have+=1

            while have==total:
                if right_best - left_best > r - l:
                    right_best, left_best = r, l
                curr[s[l]]-=1
                if curr[s[l]] < key[s[l]]:
                    have-=1
                l+=1
                
        if right_best == float('inf'):
            return ''
        return s[left_best:right_best+1]
                


