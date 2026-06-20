from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss] = [s]
        res = list(d.values())
        return res


strs = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]
res = Solution().groupAnagrams(strs)
print(output,res)

strs = [""]
output = [[""]]
res = Solution().groupAnagrams(strs)
print(output,res)

strs = ["a"]
output = [["a"]]
res = Solution().groupAnagrams(strs)
print(output,res)
