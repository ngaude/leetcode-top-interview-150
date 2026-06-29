class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        d = {}
        res = 0
        while end < len(s):
            c = s[end]
            if c in d:
                duplicate = d[c]
                if duplicate >= start:
                    start = duplicate + 1
            if end - start + 1 > res:
                res = end - start + 1
            # print(s[start:end+1],c,start,end,'res',res)
            d[c] = end
            end +=1
        return res


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("abcdefghij") == 10
assert Solution().lengthOfLongestSubstring("a") == 1
assert Solution().lengthOfLongestSubstring("a") == 1