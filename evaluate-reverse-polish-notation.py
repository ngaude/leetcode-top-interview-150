from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[-1]

tokens = ["2","1","+","3","*"]
assert Solution().evalRPN(tokens) == 9

tokens = ["4","13","5","/","+"]
assert Solution().evalRPN(tokens) == 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
assert Solution().evalRPN(tokens) == 22
