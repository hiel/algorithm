# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next

        return a == a[::-1]


print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(Solution().isPalindrome(ListNode(1, ListNode(2))))
print(Solution().isPalindrome(ListNode(1)))
