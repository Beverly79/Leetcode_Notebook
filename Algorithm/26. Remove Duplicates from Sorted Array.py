class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1] # using del will change the index
                n -= 1 # keep track of the length after deletion
            else:
                i += 1
        return i+1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
            
        return(index)