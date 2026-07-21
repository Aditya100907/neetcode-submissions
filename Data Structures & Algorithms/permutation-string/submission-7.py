from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed window, must be of size s1
        left = 0
        right = len(s1)
        need = Counter(s1)
        for i in range(len(s2)-right+1):
            if need == Counter(s2[left+i:right+i]):
                return True
        return False