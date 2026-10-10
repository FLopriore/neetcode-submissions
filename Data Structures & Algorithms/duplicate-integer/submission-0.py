class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        save_map = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in save_map.keys():
                return True
            save_map[n] = i
        return False