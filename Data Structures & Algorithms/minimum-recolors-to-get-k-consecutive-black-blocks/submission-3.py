class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_c = k + 1

        arr = []
        for b in blocks:
            if b == 'W':
                arr.append(0)
            else:
                arr.append(1)
        
        i = 0
        j = k - 1
        min_replacements = min(k, len(blocks))

        while j < len(arr):
            window = arr[i:j+1]
            ops = k - sum(window)
            min_replacements = min(min_replacements, ops)
            i += 1
            j += 1
        
        return min_replacements