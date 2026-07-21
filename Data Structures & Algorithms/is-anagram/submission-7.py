class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)




        # s2 = {}
        # t2 = {}
        # for i in s:
        #     s2[i]= s2.get(i, 0)+1
        # for i in t:
        #     t2[i] = t2.get(i, 0)+1
        # return s2 == t2



        # from collections import defaultdict
        # s_d = defaultdict(int)
        # t_d = defaultdict(int)
        # for i in s:
        #     s_d[i] +=1
        # for i in t:
        #     t_d[i] +=1
        # return s_d == t_d

        

        

        