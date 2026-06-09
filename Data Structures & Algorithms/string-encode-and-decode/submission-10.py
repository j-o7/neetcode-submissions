class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1 and len(strs[0]) == 0:
            return "''"

        if len(strs) == 1 and len(strs[0]) >= 1:
            return strs[0]

        return " , ".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        if s == "''":
            return [""]
        
        if ' , ' in s:
            return s.split(' , ')

        return [s]