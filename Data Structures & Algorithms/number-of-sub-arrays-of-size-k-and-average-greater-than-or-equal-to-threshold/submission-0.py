class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_count = 0
        i = 0
        j = k - 1

        while j < len(arr):
            win = arr[i:j+1]
            avg = sum(win) / len(win)
            if avg >= threshold:
                sub_count += 1
            
            i += 1
            j += 1
        return sub_count