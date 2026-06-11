class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        brac_dict = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for c in s:
            if c in list(brac_dict.keys()):
                i += 1
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                i -= 1
                last = stack.pop()
                if brac_dict[last] != c:
                    print(c)
                    print(brac_dict)
                    return False
            

        if len(stack) == 0 and i == 0:
            return True

        print(stack)
        print(s)
        return False
