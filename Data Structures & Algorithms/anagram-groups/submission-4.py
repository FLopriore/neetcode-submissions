class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for s in strs:
            num_letters_string = [0] * 26
            for c in s:
                num_letters_string[ord(c) - ord('a')] += 1
            
            tuple_n_lett = tuple(num_letters_string)
            if tuple_n_lett in maps.keys():
                maps[tuple_n_lett].append(s)
            else:
                maps[tuple_n_lett] = [s]
        return list(maps.values())

            