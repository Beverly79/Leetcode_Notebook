########### Time O(n)  Space O(1) ###########
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits[:-1]:
            num += i
            num *= 10
        num += digits[-1]
        num += 1
        output = []
        while num > 0:
            output.append(num % 10)
            num = num // 10
        return output[::-1]


########### Time O(n)  Space O(1) ###########
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1] # reverse
        digits.append(0)
        digits[0] += 1
        for i in range(len(digits)-1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i+1] += 1
        if digits[-1] == 0:
            digits = digits[:-1]
        return digits[::-1]