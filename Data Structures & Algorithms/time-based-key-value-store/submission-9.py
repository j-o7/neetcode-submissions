class TimeMap:

    def __init__(self):
        self.temp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.temp:
            self.temp[key].append((timestamp, value))
        else:
            self.temp[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.temp:
            return ""

        res, pairs = "", self.temp[key]
        l, r = 0, len(pairs) - 1
        if pairs[l][0] > timestamp:
            return ""

        while l <= r:
            # if (r - l) == 1:
            #     return pairs[l][1]

            mid = l + ((r - l) // 2)
            # if pairs[mid][0] == timestamp:
            #     return pairs[mid][1]

            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                l = mid + 1
            else:
                r = mid - 1


        return res
            
