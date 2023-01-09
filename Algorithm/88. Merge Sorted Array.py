class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2:
            nums1[-n:] = nums2
            nums1.sort()


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = m + n - 1 # the last index in nums1
        t1 = m - 1 # the index of the biggest number in nums1
        t2 = n - 1 # index of the biggest number in nums2
        while t2 >= 0: # start from the end to the beginning, go through nums2
            if t1 >= 0 and nums2[t2] <= nums1[t1]:
                nums1[t] = nums1[t1]# update the bigger one into nums1
                t1 -= 1 # move to the next in nums2
            else:
                nums1[t] = nums2[t2] 
                t2 -= 1
            t -= 1
        
        # if nums2 is empty, there will be no while loop, nums1 stay the same
        # if nums1 is empty, only update nums1 as nums2