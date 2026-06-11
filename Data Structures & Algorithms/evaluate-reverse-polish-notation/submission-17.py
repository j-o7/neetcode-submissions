class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # import numpy as np

        def operate(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            elif op == '/':
                return int(float(x) / y)

        stack = []
        for c in tokens:
            if c not in '+-*/':
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                res = operate(a, b, c)
                stack.append(res)
            
        return stack.pop()