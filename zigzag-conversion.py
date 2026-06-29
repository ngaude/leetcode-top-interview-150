class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if len(s) == 1:
            return s
        n = len(s)
        rows = [[] for i in range(numRows)]
        for i in range(n):
            c = s[i]
            step = i%(2*(numRows-1))
            if step < numRows:
                rows[step].append(c)
            else:
                rows[2*(numRows-1)-step].append(c)
        return ''.join([''.join(row) for row in rows])