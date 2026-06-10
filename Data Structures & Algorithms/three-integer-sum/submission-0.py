class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        idxs = []

        for i, n in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            target = -n
            # print(target)

            while j < k:
                s = nums[j] + nums[k]


                if s == target:
                    zero_list = [nums[i], nums[j], nums[k]]
                    if zero_list not in idxs:
                        idxs.append(zero_list)
                        
                    j += 1
                elif s > target:
                    k -= 1
                elif s < target:
                    j += 1

        return idxs


            