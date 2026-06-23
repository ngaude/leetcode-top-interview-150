from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        imax = min([len(s) for s in strs])
        if imax == 0:
            return ""
        lcs = []
        for i in range(0,imax):
            c = strs[0][i]
            valid = True
            for s in strs[1:]:
                if s[i] != c:
                    valid = False
                    break
            if valid == True:
                lcs.append(c)
            else:
                break
        return ''.join(lcs)

strs = ["flower","flow","flight"]
assert Solution().longestCommonPrefix(strs) == 'fl'

strs = ["flower","flower"]
assert Solution().longestCommonPrefix(strs) == 'flower'