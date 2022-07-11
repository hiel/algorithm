# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        t = {')': '(', '}': '{', ']': '['}
        for c in s:
            if len(q) == 0 or c in ['(', '{', '[']:
                q.append(c)
            elif q[-1] == t[c]:
                q.pop()
            else:
                return False
        return len(q) == 0

print(Solution().isValid('()'))
print(Solution().isValid('()[]{}'))
print(Solution().isValid('(]'))
print(Solution().isValid("(){}}{"))
