from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
       # we make a char frequency hashmap of t and use that as our universal key that we compare our window to
       # we make a char frequency hashmap of what the current window is and change it as the window changes
       # window change - expand right until window works, shrink left until it doesnt work to get smallest window, repeat
       # store what the best left and best right indices were
       # compare what a working window bounds are to best and update accordingly
       # return the substring using the best bounds
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        left = 0
        curr = defaultdict(int)
        total = len(need)
        have = 0
        best_left = 0
        best_right = float('inf')

        for i in range(len(s)):
            curr[s[i]] += 1
            if need[s[i]] == curr[s[i]]:
                have += 1
            while total == have:
                if best_right - best_left > i - left + 1:
                    best_right = i + 1
                    best_left = left
                curr[s[left]] -= 1
                if need[s[left]] > curr[s[left]]:
                    have -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1

        return s[best_left:best_right] if best_right != float('inf') else ""
            
                