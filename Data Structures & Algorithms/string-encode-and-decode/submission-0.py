class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for item in strs:
            result += str(len(item)) + "#" + item
        return result
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            lst.append(str(s[j+1:j+1+length]))
            i = j+1+length
        return lst



