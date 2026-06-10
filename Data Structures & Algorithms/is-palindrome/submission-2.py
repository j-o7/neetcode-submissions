class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "")
        s = re.findall(r'[a-zA-Z0-9]+', s)
        s = "".join(s).lower()
        if len(s) % 2 == 0:
            mid = len(s) // 2 
        else:
            mid = len(s) // 2 + 1

        # mid = len(s) // 2
        i = 0
        print(s)
        while i < mid:
            print(s[i])
            print(s[len(s) - (i+1)])
            if s[i] != s[len(s) - (i + 1)]:
                return False
            i += 1

        return True