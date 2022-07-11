# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        r = 0
        t = 0
        for c in s:
            r += (m[c] - t - t) if t < m[c] else m[c]
            t = m[c]
        return r


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
