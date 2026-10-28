from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res1 = []

        while head:
            res1.append(head.val)
            head = head.next

        return res1 == res1[::-1]