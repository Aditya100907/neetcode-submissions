from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = defaultdict(int), defaultdict(int)
        l, r = 0, 0
        for c in t:
            countT[c] += 1
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        while r < len(s):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

            r += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""