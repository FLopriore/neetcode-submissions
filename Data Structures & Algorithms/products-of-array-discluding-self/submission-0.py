class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]*len(nums)
        suffix_mul = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix_mul[i] = nums[i-1] * prefix_mul[i-1]
            suffix_mul[i] = nums[len(nums)-i] * suffix_mul[i-1]

        result = []
        for i in range(len(nums)):
            result.append(prefix_mul[i]*suffix_mul[len(nums)-i-1])
        return result

