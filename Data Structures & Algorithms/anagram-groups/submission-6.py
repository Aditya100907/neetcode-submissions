class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #naive solution: sort every str in strs in one pass, in second pass use sorted version as key of map and store originals as values, then print values
        # is there a way to go about this thats faster than sorting?
        from collections import defaultdict
        result = defaultdict(list)
        for word in strs:
            # convert to a array and then to a tuple representing each letter and how often it comes up
            key = [0]*26
            for char in word:
                key[ord(char)-ord('a')] +=1
            result[tuple(key)].append(word)
        return list(result.values())
