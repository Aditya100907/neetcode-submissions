class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        final = 0
        for val in tokens:
            if val == "+":
                final = int(stack.pop()) + int(stack.pop())
                stack.append(final)
            elif val == "-":
                final = (int(stack.pop()) - int(stack.pop()))*-1
                stack.append(final)
            elif val == "*":
                final = int(stack.pop()) * int(stack.pop())
                stack.append(final)
            elif val == "/":
                final = int(1 / float(stack.pop()) * float(stack.pop()))
                stack.append(final)
            else:
                stack.append(int(val))
        return stack.pop()
