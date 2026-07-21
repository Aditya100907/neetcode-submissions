class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        seen = set()
        for i in range (len(s)):
            while s[i] in seen:
                seen.discard(s[left])
                left+=1
            seen.add(s[i])
            best = max(best, i - left+1)
        return best