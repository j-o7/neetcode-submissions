class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = max(nums)
        nums.sort()

        i = 0
        j = k - 1
        while j < len(nums):
            win = nums[i:j+1]
            print(win)
            diff = max(win) - min(win)
            min_diff = min(diff, min_diff)
            i += 1
            j += 1
        return min_diff
