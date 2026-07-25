class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        l = 0

        for i in range(len(s1)):
            s1_char, s2_char = s1[i], s2[i]
            s1_arr[ord(s1_char) - ord('a')] += 1
            s2_arr[ord(s2_char) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_arr[i] == s2_arr[i]:
                matches+=1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_arr[index]+=1
            if s2_arr[index] == s1_arr[index]:
                matches+=1
            elif s2_arr[index] == s1_arr[index] +1:
                matches-=1
            
            index = ord(s2[r-len(s1)]) - ord('a')
            s2_arr[index]-=1
            if s2_arr[index] == s1_arr[index]:
                matches+=1
            elif s2_arr[index] == s1_arr[index] -1:
                matches-=1

        
        return matches == 26
