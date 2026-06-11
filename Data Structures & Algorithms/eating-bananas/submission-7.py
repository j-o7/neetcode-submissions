class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        min_k = 1

        return_k = max_k + 1

        while min_k <= max_k:
            mid_k = min_k + ((max_k - min_k) // 2)
            ch = 0
            for p in piles:
                ph = math.ceil(p / mid_k)
                ch += ph            
            if ch <= h and mid_k < return_k:
                return_k = mid_k            
            if ch > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k - 1
            
        return return_k


            