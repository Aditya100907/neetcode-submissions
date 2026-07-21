class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_d = defaultdict(int)
        t_d = defaultdict(int)
        for i in s:
            s_d[i] +=1
        for i in t:
            t_d[i] +=1
        return s_d == t_d

        

        

        