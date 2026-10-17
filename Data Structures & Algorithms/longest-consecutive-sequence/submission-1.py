class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        nums_set = set(nums)
        for n in nums:
            if n-1 not in nums_set:
                j = n
                while j+1 in nums_set:
                    j += 1
                curr_length = j + 1 - n
                max_length = max(max_length, curr_length)
        
        return max_length