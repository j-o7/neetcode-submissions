class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cur_sum = sum(arr[:k])
        if cur_sum / k >= threshold:
            res += 1
        for r in range(k, len(arr)):
            cur_sum -= arr[r-k]
            cur_sum += arr[r]
            if cur_sum / k >= threshold:
                res += 1

        return res
        # sub_count = 0
        # i = 0
        # j = k - 1

        # while j < len(arr):
        #     win = arr[i:j+1]
        #     avg = sum(win) / len(win)
        #     if avg >= threshold:
        #         sub_count += 1
            
        #     i += 1
        #     j += 1
        # return sub_count