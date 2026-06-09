class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for n in nums:
            if n in temp:
                temp[n] += 1
            else:
                temp[n] = 1

        sorted_temp = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True))

        return list(sorted_temp.keys())[:k]