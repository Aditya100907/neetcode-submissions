from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        
        total = len(need)
        have = 0
        window = defaultdict(int)
        left = 0
        best_left, best_right = 0, float('inf')

        for right in range(len(s)):
            window[s[right]] += 1
            
            # did this char just become satisfied?
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == total:
                # is this the best window so far?
                if right - left < best_right - best_left:
                    best_left = left
                    best_right = right
                
                # shrink from left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        
        return "" if best_right == float('inf') else s[best_left:best_right+1]