from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = 0, 0
        ha, hb = headA, headB
        while ha:
            a += 1
            ha = ha.next
        while hb:
            b += 1
            hb = hb.next

        # 先走差值步
        ha, hb = headA, headB
        if a > b:
            for _ in range(a - b):
                ha = ha.next
        else:
            for _ in range(b - a):
                hb = hb.next

        while ha and hb:
            if ha == hb:       # 比较节点
                return ha
            ha = ha.next
            hb = hb.next

        return