class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ", "")
        s = re.findall(r'[a-zA-Z0-9]+', s)
        s = "".join(s).lower()
        
        i = 0
        mid = len(s) // 2
        if len(s) % 2 != 0:
            mid += 1

        while i < mid:
            print(s[i])
            print(s[len(s) - (i+1)])
            if s[i] != s[len(s) - (i + 1)]:
                return False
            i += 1

        return True