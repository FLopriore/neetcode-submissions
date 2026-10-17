import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = set(string.ascii_lowercase + string.ascii_uppercase + string.digits)

        clean_str = ""
        for c in s:
            if c in alphanum:
                clean_str += c
        
        for i in range(len(clean_str)//2):
            if clean_str[i].lower() != clean_str[len(clean_str)-i-1].lower():
                return False
        return True