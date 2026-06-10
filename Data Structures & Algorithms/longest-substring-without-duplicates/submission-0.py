class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        uniq = set(s)
        uniq_len = len(uniq)
        if uniq_len == 1:
            return 1

        for i, c in enumerate(s):
            ss = c
            j = 1
            while j < uniq_len:
                if i + j >= len(s):
                    break
                new_c = s[i+j]
                if new_c not in ss:
                    ss += new_c
                    max_len = max(len(ss), max_len)
                    j += 1
                else:
                    break

        return max_len
