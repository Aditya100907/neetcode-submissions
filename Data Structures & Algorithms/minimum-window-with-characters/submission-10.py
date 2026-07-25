from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap, smap = defaultdict(int), defaultdict(int)
        res, reslen = [-1, -1], float('infinity')
        if t == "" or len(t) > len(s):
            return ""
        for c in t:
            tmap[c]+=1
        l = 0
        have, need = 0, len(tmap)
        for r in range(len(s)):
            smap[s[r]]+=1
            if smap[s[r]]==tmap[s[r]]:
                have+=1
            while have == need:
                if r-l+1 < reslen:
                    res = [l, r+1]
                    reslen = r-l+1
                smap[s[l]]-=1
                if smap[s[l]] < tmap[s[l]]:
                    have-=1
                l+=1
        l, r = res
        if reslen != float('infinity'):
            return s[l:r]
        return ""

