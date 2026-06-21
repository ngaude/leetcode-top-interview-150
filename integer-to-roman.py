class Solution:
    def intToRoman(self, num: int) -> str:
        s = []
        while num > 0:
            if num >= 1000:
                s.append('M')
                num -= 1000
            elif num >= 900:
                s.append('CM')
                num -= 900
            elif num >= 500:
                s.append('D')
                num -= 500
            elif num >= 400:
                s.append('CD')
                num -= 400
            elif num >= 100:
                s.append('C')
                num -= 100
            elif num >= 90:
                s.append('XC')
                num -= 90
            elif num >= 50:
                s.append('L')
                num -= 50
            elif num >= 40:
                s.append('XL')
                num -= 40
            elif num >= 10:
                s.append('X')
                num -= 10
            elif num >= 9:
                s.append('IX')
                num -= 9
            elif num >= 5:
                s.append('V')
                num -= 5
            elif num >= 4:
                s.append('IV')
                num -= 4
            else:
                s.append('I')
                num -= 1
        return ''.join(s)

num = 3749
output = "MMMDCCXLIX"
assert Solution().intToRoman(num) == output

num = 58
output = "LVIII"
assert Solution().intToRoman(num) == output

num = 1994
output = "MCMXCIV"
assert Solution().intToRoman(num) == output



