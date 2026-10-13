class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = {}
        for n in nums:
            if n not in nums_freq.keys():
                nums_freq[n] = 1
            else:
                nums_freq[n] += 1
        
        freq_list = [[] for _ in range(len(nums)+1)]
        for el in nums_freq.keys():
            freq = nums_freq[el]
            freq_list[freq].append(el)
        
        result = []
        for l in reversed(freq_list):
            if len(l) == 0:
                continue
            elif k <= 0:
                break
            
            for n in l:
                if k<=0:
                    break
                result.append(n)
                k -= 1
        return result