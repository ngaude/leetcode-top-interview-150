class Solution:
    def reverseBits(self, n: int) -> int:
        b = []
        while n:
            b.append(n&1)
            n = n>>1
        n = 0
        print(b)
        for i in b:
            n = (n<<1) + i
        n = n<<(32-len(b))
        return n