class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i, n in enumerate(nums):
            temp = output[i]

            output = [output[i] * n for i in range(len(output))]

            output[i] = temp

        return output

            