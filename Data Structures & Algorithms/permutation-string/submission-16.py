class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        l,r = 0, len(s1)

        for i in range(len(s1)):
            s1_char, s2_char = s1[i], s2[i]
            s1_arr[ord(s1_char) - ord('a')] += 1
            s2_arr[ord(s2_char) - ord('a')] += 1
        
        while r < len(s2):
            if s1_arr == s2_arr:
                return True
            else:
                s2_arr[ord(s2[r]) - ord('a')]+=1
                s2_arr[ord(s2[l])-ord('a')]-=1
                r+=1
                l+=1
        return s1_arr==s2_arr

        # matches = 0
        # for i in range(26):
        #     if s1_arr[i] == s2_arr[i]:
        #         matches += 1

        # if matches == 26:
        #     return True
        
        # for i in range(len(s1_arr), len(s2_arr)):
        #     s2_char = s2_arr[i]
        #     s2_arr[ord(s2_char) - ord('a')] += 1

        
