class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        n = 0
        i = 0
        while i < l:
            if s[i] == 'I':
                if i+1<l and s[i+1] == 'V':
                    n += 4
                    i += 1
                elif i+1<l and s[i+1] == 'X':
                    n += 9
                    i += 1
                else:
                    n += 1
            elif s[i] == 'V':
                n += 5
            elif s[i] == 'X':
                if i+1<l and s[i+1] == 'L':
                    n += 40
                    i += 1
                elif i+1<l and s[i+1] == 'C':
                    n += 90
                    i += 1
                else:
                    n += 10
            elif s[i] == 'L':
                n += 50
            elif s[i] == 'C':
                if i+1<l and s[i+1] == 'D':
                    n += 400
                    i += 1
                elif i+1<l and s[i+1] == 'M':
                    n += 900
                    i += 1
                else:
                    n += 100
            elif s[i] == 'D':
                n += 500
            elif s[i] == 'M':
                n += 1000
            i+=1
        return n
            

s = "III"
output = 3
assert Solution().romanToInt(s) == output

s = "LVIII"
output = 58
assert Solution().romanToInt(s) == output

s = "MCMXCIV"
output = 1994
assert Solution().romanToInt(s) == output
