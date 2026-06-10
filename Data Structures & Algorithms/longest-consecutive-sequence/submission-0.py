class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)

        res = 0
        cnt = 0

        for n in nums:
            if n in uniq and (n - 1) not in uniq:
                cnt = 0
                cur = n
                while cur in uniq:
                    uniq.remove(cur)
                    cur += 1
                    cnt += 1
                
                res = max(res, cnt)

        return res

            

            
        