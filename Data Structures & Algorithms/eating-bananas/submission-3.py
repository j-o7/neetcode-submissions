class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import numpy as np
        max_k = max(piles)

        min_k = 1

        return_k = max_k + 1

        while min_k <= max_k:
            print(min_k)
            print(max_k)
            mid_k = min_k + ((max_k - min_k) // 2)
            print(mid_k)
            ch = 0
            for p in piles:
                ph = np.ceil(p / mid_k)
                ch += ph
            
            print(ch)
            
            if ch <= h and mid_k < return_k:
                return_k = mid_k
                print(return_k)
            
            if ch > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k - 1
            
        return return_k


            