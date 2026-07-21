from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        for word in strs:
            key = [0] * 26
            N = len(word)
            for i in range (N):
                key[ord(word[i]) - ord('a')] +=1
            d[tuple(key)].append(word)

        return list(d.values())



#act and cat are the same --> sort both strings in alphabetical order