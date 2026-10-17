class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            sum_ptr = numbers[l] + numbers[r]
            if sum_ptr == target:
                return [l+1, r+1]
            elif sum_ptr > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]