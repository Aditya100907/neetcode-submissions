from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed window, must be of size s1
        left = 0
        right = len(s1)
        s1 = Counter(s1)
        for i in range (len(s2)):
            s3 = Counter(s2[left:right+i])
            found = 0
            for key in s1:
                if s3[key] == s1[key]:
                    found+=1
            if found == len(s1):
                return True
            left+=1
        return False