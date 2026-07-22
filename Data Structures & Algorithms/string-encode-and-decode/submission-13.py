class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        output = []
        curr = 0
        while curr < len(s):
            start = curr
            while s[curr] != "#":
                curr+=1
            num = int(s[start:curr])
            word = str(s[curr+1:curr+1+num])
            output.append(word)
            curr = curr+1+num
        return output
