from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord(s) - ord('a'), array representing all letters in alphbt, convert that to a tuple
        groups = defaultdict(list)
        for word in strs:
            buckets = [0]*26
            for s in word:
                buckets[ord(s)-ord('a')] +=1
            groups[tuple(buckets)].append(word)
            
        return list(groups.values())
            