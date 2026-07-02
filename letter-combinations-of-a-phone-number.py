from typing import Optional,List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l = ['']
        for digit in digits:
            _l = []
            for e in l:
                for c in d[digit]:
                    _l.append(e+c)
            l = _l
        return l

ret = Solution().letterCombinations('23')
print(ret)

ret = Solution().letterCombinations('22')
print(ret)
        