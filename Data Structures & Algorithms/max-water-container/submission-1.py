class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        k = len(heights) - 1
        max_w = 0

        while i < k:
            s = heights[i]
            e = heights[k]

            min_h = min(s, e)

            area = (k - i) * min_h

            if area > max_w:
                max_w = area

            if s < e:
                i += 1
            else:
                k -= 1

        return max_w