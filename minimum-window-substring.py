from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        tidx = {k:-1 for k in tcount}
        tval = {k:[-1]*tcount[k] for k in tcount}
        tmin = -1
        tmax = len(s)
        tlen = 0
        res = ""
        rlen = 0
        for i in range(len(s)):
            c = s[i]
            if c in tcount:
                tidx[c] +=1
                if tidx[c] < tcount[c]:
                    tlen+=1
                idx = tidx[c] % tcount[c]
                if tmin == -1 or tmin == tval[c][idx]:
                    # compute the new tmin...
                    tval[c][idx] = i
                    values  = [b for a in tval.values() for b in a if b>=0]
                    if len(values):
                        tmin = min(values)
                else:
                    tval[c][idx] = i
                tmax = i
                if len(t) == tlen:
                    if rlen == 0 or tmax - tmin + 1 < len(res):
                        res = s[tmin:tmax+1]
                        rlen = len(res)
        return res

                 

    def minWindow_naive(self, s: str, t: str) -> str:
        d = {}
        ls = len(s)
        lt = len(t)
        res = ''
        for i in range(ls):
            c = s[i]
            if c in t:
                d[c] = i
            if len(d) == lt:
                tmin = min(d.values())
                tmax = max(d.values())
                if len(res) == 0 or tmax - tmin + 1 < len(res):
                    res = s[tmin:tmax+1]
        return res

s = "ADOBECODEBANC"
t = "ABC"
assert Solution().minWindow(s,t) == 'BANC'

s = "a"
t = "a"
assert Solution().minWindow(s,t) ==  "a"

s = "a"
t = "aa"
assert Solution().minWindow(s,t) ==  ""


s = "aa"
t = "aa"
assert Solution().minWindow(s,t) ==  "aa"


s = "cabwefgewcwaefgcf"
t = "cae"
assert Solution().minWindow(s,t) ==  "cwae"