class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            print("returning None")
            return ""

        if len(strs) == 1 and len(strs[0]) == 0:
            return "''"

        if len(strs) == 1 and len(strs[0]) >= 1:
            return strs[0]

        return " , ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        if s == "''":
            return [""]
        
        if ' , ' in s:
            return s.split(' , ')

        return [s]