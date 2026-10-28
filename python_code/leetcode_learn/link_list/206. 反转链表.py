from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1.遍历，然后直接新建链表
# 2.原地反转，三指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        while head != None:

            next_node = head.next
            head.next = pre
            pre = head
            head = next_node

        return pre


