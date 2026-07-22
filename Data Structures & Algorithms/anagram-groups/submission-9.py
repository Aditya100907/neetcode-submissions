from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            rep = [0]*26
            for s in word:
                rep[ord(s) - ord('a')] += 1
            anagrams[tuple(rep)].append(word)
        return list(anagrams.values())