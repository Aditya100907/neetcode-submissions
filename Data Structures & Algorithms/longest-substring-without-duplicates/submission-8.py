class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, longest = 0, 0, 0
        window = set()
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r+=1
                longest = max(longest, r-l)
            else:
                window.discard(s[l])
                l+=1
        return longest
