########### Time O(log(n))  Space O(1) ###########
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        low = 0
        high = len(nums)
        while high > low:
            mid = (high+low)//2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                return mid
        return low


########### Time O(log(n))  Space O(1) ###########
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bisect
        import bisect
        return bisect_left(nums, target)
