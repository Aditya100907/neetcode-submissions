class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in p:
                if not stack or stack[-1] != p[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
