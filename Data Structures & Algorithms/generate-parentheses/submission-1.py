class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack (opened, closed, current):
            if opened+closed == 2*n:
                result.append(current)
            if opened < n:
                backtrack(opened+1, closed, current + '(')
            if closed < opened:
                backtrack(opened, closed+1, current + ')')
        backtrack(0, 0, '')
        return result