class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif t == "-":
                stack.append((int(stack.pop())-int(stack.pop()))*-1)
            elif t == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif t == "/":
                stack.append(int(1 / float(stack.pop()) * float(stack.pop())))
            else:
                stack.append(int(t))
        return stack[0]