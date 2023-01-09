########### Time O(n)  Space O(n) ###########
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)[0]


########### Time O(n)  Space O(1) ###########
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor

'''
Example:
1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 (commutative & associative)
= 0 xor 0 xor 0 xor 4
= 4
'''