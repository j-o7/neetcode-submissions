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
                div_str = str(x / y)
                return int(div_str.split('.')[0])

        stack = []
        ops = ['+', '-', '*', '/']
        print(tokens)
        for c in tokens:
            if c not in ops:
                stack.append(c)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                res = operate(a, b, c)
                stack.append(str(res))
            print(stack)

        if len(stack) > 1:
            print(stack)
        return int(stack.pop())