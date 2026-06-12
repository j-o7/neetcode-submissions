class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for i, n in enumerate(nums):
            if n not in temp:
                temp[n] = i
            else:
                diff = i - temp[n]
                if diff <= k:
                    return True
                else:
                    temp[n] = i

        return False
        # for key, idxs in temp.items():
        #     for