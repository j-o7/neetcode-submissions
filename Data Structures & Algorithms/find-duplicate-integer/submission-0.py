class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()
        
        for n in nums:
            if n not in uniq:
                uniq.add(n)
            else:
                return n