from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        fin_res = []
        for v in res:
            if not fin_res or v != fin_res[-1]:
                fin_res.append(v)

        dummy = ListNode(0)  # dummy
        cur = dummy
        for v in fin_res:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next