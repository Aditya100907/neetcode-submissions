from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        key = defaultdict(int)
        for char in t:
            key[char]+=1
        best_left = 0
        left = 0
        best_right = float('inf')
        total = len(key)
        have = 0
        curr = defaultdict(int)
        for i in range (len(s)):
            curr[s[i]]+=1
            if curr[s[i]]==key[s[i]]:
                have+=1
            while have == total:
                if best_right - best_left > i - left:
                    best_right, best_left = i, left
                curr[s[left]]-=1
                if curr[s[left]] < key[s[left]]:
                    have-=1
                left+=1
        if best_right != float('inf'):
            return s[best_left:best_right+1]
        else:
            return ""

