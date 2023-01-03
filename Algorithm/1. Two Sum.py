########### Time O(n^2)  Space O(1) ###########
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]


########### Time O(n)  Space O(n) ###########

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dic:
                return [dic[dif], i]
            else:
                dic[nums[i]] = i