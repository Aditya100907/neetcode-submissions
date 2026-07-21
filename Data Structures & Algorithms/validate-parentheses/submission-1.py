class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')':'(', '}':'{', ']':'['}
        closing = {']', '}', ')'}
        
        for i in range(len(s)):
            if s[i] in closing:
                if not stack or stack[-1] != parentheses[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        
        return not stack
