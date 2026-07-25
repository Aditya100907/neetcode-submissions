class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1arr, s2arr = [0]*26, [0]*26
        l = 0
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s1arr[ord(s1[i])- ord('a')]+=1
            s2arr[ord(s2[i])-ord('a')]+=1
        
        matches = 0
        for i in range(26):
            if s1arr[i]==s2arr[i]:
                matches+=1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r])-ord('a')
            s2arr[index]+=1
            if s2arr[index]==s1arr[index]:
                matches+=1
            elif s2arr[index] == s1arr[index]+1:
                matches-=1
            index = ord(s2[l])-ord('a')
            s2arr[index] -=1
            if s2arr[index]==s1arr[index]:
                matches+=1
            elif s2arr[index] == s1arr[index]-1:
                matches-=1
            l+=1

        return matches==26
