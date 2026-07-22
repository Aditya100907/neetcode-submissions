class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest, currl = 0, 0
        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                currl+=1
                longest = max(currl, longest)
            else:
                seen.discard(s[left])
                left+=1
                currl-=1
        return longest
            
