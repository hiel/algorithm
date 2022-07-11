# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        try:
            for i in range(len(strs[0])):
                t = strs[0][i]
                for s in strs[1:]:
                    if t != s[i]:
                        return r
                r += t
        except Exception:
            pass
        return r

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
