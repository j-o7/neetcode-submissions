class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        uniq = Counter(nums)
        first_val = None
        second_val = None
        print(uniq)

        for k, v in uniq.items():
            diff = target - k
            print(k, v)
            if diff == k and v > 1:
                print(k, v)
                first_val = k
                second_val = k
                idxs = [i for i, x in enumerate(nums) if x == k]
                first_return = idxs[0]
                second_return = idxs[1]
                break
            if diff == k and v == 1:
                continue
            if diff in uniq.keys():
                first_val = k
                second_val = diff
                first_idx = [i for i, x in enumerate(nums) if x == first_val]
                second_idx = [i for i, x in enumerate(nums) if x == second_val]

                i = 0
                j = 0
                first_return = first_idx[i]
                second_return = second_idx[j]

                break

        # if first_val and second_val:
        #     first_idx = [i for i, x in enumerate(nums) if x == first_val]
        #     second_idx = [i for i, x in enumerate(nums) if x == second_val]

        #     i = 0
        #     j = 0
        #     first_return = first_idx[i]
        #     second_return = second_idx[j]

        #     while first_return == second_return:
        #         print(first_return)
        #         print(second_return)
        #         if i <= j:
        #             i = i + 1
        #             first_return = first_idx[i]
        #             print(first_return)
        #         else:
        #             j = j + 1
        #             second_return = second_idx[j]
        # else:
        #     return False

        # for n in uniq:
        #     diff = target - n
        #     if diff in uniq:
        #         first_idx = nums.index(diff)
        #         second_idx = nums.index(n)
        #         break

        if first_return > second_return:
            temp = first_return
            first_return = second_return
            second_return = first_return
            
        return [first_return, second_return]
        