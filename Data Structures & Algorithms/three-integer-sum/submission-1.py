class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set([])
        for i in range(len(nums)):
            target_sum = -nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                curr = nums[l] + nums[r]
                if curr > target_sum:
                    r -= 1
                elif curr < target_sum:
                    l += 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
        return list(res)