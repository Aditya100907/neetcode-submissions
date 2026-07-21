from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        need = Counter(s1)
        curr = Counter(s2[:k])
        if need == curr:
            return True
        for i in range(k, len(s2)):
            curr[s2[i - k]] -= 1
            if curr[s2[i-k]] == 0:
                del curr[s2[i-k]]
            curr[s2[i]] +=1
            if need == curr:
                return True
        return False
