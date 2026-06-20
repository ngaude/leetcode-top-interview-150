class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a),len(b))
        carry = 0
        res = []
        for i in range(n):
            da = int(a[len(a)-i-1]) if (len(a)-i-1 >= 0)  else 0
            db = int(b[len(b)-i-1]) if (len(b)-i-1 >= 0)  else 0
            s = da + db + carry
            res.append(str(s % 2))
            carry = s//2
        if carry > 0:
            res.append('1')
        res = ''.join(res[::-1])
        return res

a = "1"
b = "111"
Solution().addBinary(a,b)

        

a = "11"
b = "1"
output = "100"
assert Solution().addBinary(a,b) == output


a = "1010"
b = "1011"
output = "10101"
assert Solution().addBinary(a,b) == output