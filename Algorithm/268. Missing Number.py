########### Time O(n)  Space O(1) ###########
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0] != 0: # miss the first one
            return 0 # this include [1], which means 0 is missing
        for i in range(n-1):
            if nums[i+1] - nums[i] == 2: # missing in the middle
                return nums[i] + 1
        return n # miss the last one


########### Time O(1)  Space O(1) ###########
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        full_sum = (0 + n) * (n + 1) // 2 # sum of first n numbers using Gaus formula
        return full_sum - sum(nums)