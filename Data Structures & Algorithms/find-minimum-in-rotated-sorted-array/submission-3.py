class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] >= nums[l] and nums[m] < nums[r]:
                return nums[l]
            if m == l:
                return nums[r]
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m
                continue
            if nums[m] < nums[l] and nums[m] < nums[r]:
                r = m
                continue

        # return nums[r + 1]
        