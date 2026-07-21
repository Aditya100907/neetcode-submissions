class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s:
            if c.isalnum():
                result+=c
        s = result.lower()
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True