class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        res = 0
        sign = 1
        while i < len(s):
            c = s[i]
            if c == '-':
                sign = -sign
                i += 1
                continue
            if c in '1234567890':
                # parse val
                val = int(c)
                i += 1
                while i < len(s):
                    c = s[i]
                    if c in '1234567890':
                        val = val * 10 + int(c)
                    else:
                        break
                    i+=1
                res += val * sign
                sign = 1
                continue
            if c == ' ':
                i+=1
                continue
            if c == '+':
                i+=1
                continue
            if c == '-':
                i+=1
                sign = -sign
                continue
            if c == '(':
                # push current status on stack
                stack.append((res,sign))
                res = 0
                sign = 1
                i+=1
                continue
            if c == ')':
                _res, _sign = stack.pop()
                res = _res + res*_sign
                i+=1
                continue
            i+=1
        return res
    
    def calculate_recursive(self, s: str) -> int:
        i = 0
        res = 0
        sign = 1
        while i < len(s):
            c = s[i]
            if c == '-':
                sign = -sign
                i += 1
                continue
            if c in '1234567890':
                # parse val
                val = int(c)
                i += 1
                while i < len(s):
                    c = s[i]
                    if c in '1234567890':
                        val = val * 10 + int(c)
                    else:
                        break
                    i+=1
                res += val * sign
                sign = 1
                continue
            if c == ' ':
                i+=1
                continue
            if c == '+':
                i+=1
                continue
            if c == '-':
                i+=1
                sign = -sign
                continue
            if c == '(':
                # parse enclosure
                l = 1
                start = i+1
                while l > 0:
                    i += 1
                    c = s[i]
                    if c == '(':
                        l += 1
                    elif c == ')':
                        l -= 1
                res += sign * self.calculate(s[start:i])
                sign = 1
                i+=1
                continue
            i+=1
        return res
    

s = "1-(     -2)"
assert Solution().calculate(s) ==  3

s = "1 + 1"
assert Solution().calculate(s) == 2

s = " 2-1 + 2 "
assert Solution().calculate(s) == 3

s = "(1+(4+5+2)-3)+(6+8)"
assert Solution().calculate(s) == 23

s = '1-(1-1)-1'
assert Solution().calculate(s) ==  0

s = "1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10"
assert Solution().calculate(s) ==  -15