class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in nums_map.keys() and nums_map[y] != i:
                return [min(i, nums_map[y]), max(i, nums_map[y])]
            nums_map[x] = i
        return []
        