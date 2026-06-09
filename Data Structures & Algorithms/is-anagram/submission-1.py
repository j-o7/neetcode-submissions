class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = set(list(s))
        t_chars = set(list(t))

        if len(s_chars) != len(t_chars):
            return False

        for c in s_chars:
            if c not in t_chars:
                return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        for c in s_chars:
            if s_count[c] != t_count[c]:
                return False

        return True