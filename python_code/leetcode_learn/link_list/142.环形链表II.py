"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

- 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
- 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
- 如果 pos 是 -1，则在该链表中没有环。
【注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。】
"""
from logging import setLoggerClass
from typing import Optional

"""
思路：floyd判图法？
1. 确定是否有环：floyd判圈法
2. 找入口：slow = head， fast = meet， 一起加速，相遇即为入口
3. 返回节点
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:    # 开始找入口
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

