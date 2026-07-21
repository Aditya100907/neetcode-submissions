class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make hash table of each and then check if both are same
        # h1 = {}
        # h2 = {}
        # for letter in s:
        #     h1[letter] = h1.get(letter, 0) + 1
        # for letter in t:
        #     h2[letter] = h2.get(letter, 0) + 1
        # if h1 == h2:
        #     return True
        # return False
        from collections import Counter
        return Counter(s) == Counter(t)
        
        