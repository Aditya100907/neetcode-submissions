from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                #need to make some universal key for the anagrams
        #could sort the anagrams but thats slower, it multplies logn to the complexity - should be a 26 long tuple representing the frequency of each letter computed using ord for each letter
        # need one for loop to go through each word, one for loop to go through its characters and create the tuple key
        # create a defaultdict and add to it and create a frequency map of prevalence of the canonical form
        d = defaultdict(list)
        for my in strs:
            key = [0]*26
            for s in my:
                key[ord(s) - ord("a")] += 1
            d[tuple(key)].append(my)
        return list(d.values())