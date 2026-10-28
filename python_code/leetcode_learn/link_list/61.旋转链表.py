from typing import Optional

"""
思路：
1. 计算链表长度n
2. 取模：有效旋转次数k = k % n
3. 定位新尾节点：原链表的n-k-1个节点会成为尾部，下一个节点就是新头节点
4. 重新连接：
5. 返回新头节点：
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # 遍历长度n
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k = k % n
        if k == 0:
            return head
        cur = head
        for _ in range(n-k-1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head