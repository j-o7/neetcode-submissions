class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(x: str, y: str) -> bool:
            x_count = Counter(x)
            y_count = Counter(y)

            if len(x_count) != len(y_count):
                return False

            for x in x_count.keys():
                if x not in y_count:
                    return False
                
                if x_count[x] != y_count[x]:
                    return False

            return True

        output_list = []
        i = 0
        while len(strs) != 0:
            j = 0
            cur_list = []
            
            cur_list.append(strs[i])
            del strs[i]
            while j < len(strs):
                is_anag = is_anagram(cur_list[0], strs[j])
                if is_anag:
                    cur_list.append(strs[j])
                    del strs[j]
                else:
                    j = j + 1


            output_list.append(cur_list)

        return output_list
