class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i != j:
            # if numbers[j] >= target:
            #     j -= 1
            #     continue

            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
                continue

            if sum < target:
                i += 1
                continue
            
            if sum == target:
                return [i+1, j+1]