class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            ri = m // COLS
            ci = m % COLS
            if matrix[ri][ci] > target:
                r = m - 1
            elif matrix[ri][ci] < target:
                l = m + 1
            else:
                return True
            
        return False
        # cols = [x[0] for x in matrix]
        # cl, cr = 0, len(cols) - 1
        # ci = -1
        # while cl < cr:
        #     if cr - cl == 1:
        #         if cols[cl] == target or cols[cr] == target:
        #             return True
        #         if cols[cr] < target:
        #             ci = cr
        #         else:
        #             ci = cl
        #         break
        #     cm = cl + ((cr - cl) // 2)
        #     if cols[cm] == target:
        #         return True

        #     if cols[cm] < target:
        #         cl = cm
        #     else:
        #         cr = cm
        
        # row = matrix[ci]
        # rl, rr = 0, len(row) - 1
        # while rl < rr:
        #     rm = rl + ((rr - rl) // 2)
        #     if row[rm] == target:
        #         return True
            
        #     if row[rm] > target:
        #         rr = rm - 1
        #     else:
        #         rl = rm + 1
        
        # if row[rl] == target:
        #     return True

        # return False
