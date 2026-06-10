class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = max(prices)
        p = 0

        for n in prices:
            m = min(m, n)
            t = n - m
            if t > p:
                p = t

        return p

        