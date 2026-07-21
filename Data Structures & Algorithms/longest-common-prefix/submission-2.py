class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = 0
        for i in range(len(strs[0])):
            count = 0
            init = strs[0][common]
            for word in strs:
                if len(word) <= common:
                    return strs[0][:common]
                if word[common]==init:
                    count+=1
            if count % len(strs) == 0:
                common+=1
            else:
                break
        return strs[0][:common]
