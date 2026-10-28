
from typing import Optional
"""
思路：
1. 边界处理：如果链表为空或者只有一个节点，删除中间节点后链表为空，直接返回none
2. 快慢指针定位中间节点：(因为删除中间节点，所以直接slow移动一步，fast移动二步，fast到达链表尾部时，slow正好在中间节点)
    维护prev指针，记录slow的前一个节点，用于删除
3. 删除节点：将prev.next指向slow.next
4. 返回头节点
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return None
            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            prev.next = slow.next
            return head
