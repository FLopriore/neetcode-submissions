class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0
        num_digits = ""
        while i < len(s):
            if s[i] == "#":
                s_len = int(num_digits)
                extracted_str = s[i+1:i+1+s_len]
                i += s_len
                result.append(extracted_str)
                num_digits = ""
            else:
                num_digits += s[i]
            i += 1
        
        return result