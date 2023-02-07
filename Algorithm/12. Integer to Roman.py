class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1}
        l_symbol = list(dic.keys())
        output = ""
        res = num
        for i in l_symbol:
            rep = res // dic[i]
            output += i * rep # we can simply repeat strings by multiplication instead of a for loop
            res = res % dic[i]

        return output
