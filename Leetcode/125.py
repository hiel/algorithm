# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for c in s:
            if c.isalnum():
                t += c.lower()
        for i in range(int(len(t)/2)):
            if t[i] != t[-i-1]:
                return False
        return True


print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution().isPalindrome('race a car'))
print(Solution().isPalindrome(' '))
