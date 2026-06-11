class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        print(mid)
        print(nums)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            print('before')
            res = self.search(nums[:mid], target)
            print(res)
            if res == -1:
                return -1
            else:
                return res
        else:
            print('after')
            res = self.search(nums[mid+1:], target)
            print(res)
            if res == -1:
                return -1
            else:
                return mid + res + 1

        # return -1