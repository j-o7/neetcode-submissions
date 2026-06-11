class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = [x[0] for x in matrix]
        cl, cr = 0, len(cols) - 1
        ci = -1
        while cl < cr:
            print(cl)
            print(cr)
            if cr - cl == 1:
                if cols[cl] == target or cols[cr] == target:
                    return True
                if cols[cr] < target:
                    ci = cr
                else:
                    ci = cl
                break
            cm = cl + ((cr - cl) // 2)
            print(cm)
            if cols[cm] == target:
                return True

            if cols[cm] < target:
                cl = cm
            else:
                cr = cm
        


        row = matrix[ci]
        rl, rr = 0, len(row) - 1
        while rl < rr:
            rm = rl + ((rr - rl) // 2)
            print(rl)
            print(rr)
            print(row[rm])
            if row[rm] == target:
                return True
            
            if row[rm] > target:
                rr = rm - 1
            else:
                rl = rm + 1
        
        if row[rl] == target:
            return True

        return False
