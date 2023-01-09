class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                del nums[i]
                n -= 1
            else:
                i += 1
        return i