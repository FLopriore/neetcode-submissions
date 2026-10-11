from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_indexes_letters = {}
        for idx in range(26):
            dict_indexes_letters[ascii_lowercase[idx]] = idx

        maps = {}
        for s in strs:
            num_letters_string = [0] * 26
            for c in s:
                num_letters_string[dict_indexes_letters[c]] += 1
            
            tuple_n_lett = tuple(num_letters_string)
            
            if tuple_n_lett in maps.keys():
                maps[tuple_n_lett].append(s)
            else:
                maps[tuple_n_lett] = [s]
        
        result = []
        for k in maps.keys():
            result.append(maps[k])
        return result

            