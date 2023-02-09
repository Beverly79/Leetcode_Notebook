# Time complexity : O(n!). Total possible permutations is n!n!n!.
# Space complexity : O(n). Since an array will be used to store the permutations. 

class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 5, 3, 2] -> [5, 1, 2, 3]
        mark = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                # [i-1] is the idx where we wanna reorder.
                # the first number should be the one slightly bigger than nums[i-1]
                # out of nums[i:]
                temp = sorted(nums[i-1:])
                for n in temp:
                    if n > nums[i-1]:
                        start = n
                        break
                temp.remove(n)
                nums[i-1] = n
                nums[i:] = temp
                mark = 1
                break
        if mark == 0:
            nums.sort()


# slightly faster because nums[i:] is sorted (descending) after the swap
class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 5, 3, 2] -> [5, 1, 2, 3]
        mark = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                # [i-1] is the idx where we wanna reorder.
                # the first number should be the one slightly bigger than nums[i-1]
                # out of nums[i:]
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        # nums[j] is the new starting number,
                        # we swap nums[j] and nuns[i-1]
                        temp = nums[j]
                        nums[j] = nums[i-1]
                        nums[i-1] = temp
                        break
                # now nums[i:] is sorted (descending)
                nums[i:] = nums[i:][::-1]
                mark = 1
                break
        if mark == 0:
            nums.sort()

