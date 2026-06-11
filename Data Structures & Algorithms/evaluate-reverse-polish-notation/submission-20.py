class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                if c == '+':
                    res =  a + b
                elif c == '-':
                    res =  a - b
                elif c == '*':
                    res =  a * b
                elif c == '/':
                    res =  int(float(a) / b)
                stack.append(res)
            
        return stack.pop()