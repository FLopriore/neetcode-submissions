import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}
        for ch in s:
            if ch not in freq_s.keys():
                freq_s[ch] = 1
            else:
                freq_s[ch] += 1
        
        freq_t = {}
        for ch in t:
            if ch not in freq_t.keys():
                freq_t[ch] = 1
            else:
                freq_t[ch] += 1
        
        if freq_s == freq_t:
            return True
        return False
