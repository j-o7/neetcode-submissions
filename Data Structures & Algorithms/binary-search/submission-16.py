class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            res = self.search(nums[:mid], target)
            if res == -1:
                return -1
            else:
                return res
        else:
            res = self.search(nums[mid+1:], target)
            if res == -1:
                return -1
            else:
                return mid + res + 1

        # return -1