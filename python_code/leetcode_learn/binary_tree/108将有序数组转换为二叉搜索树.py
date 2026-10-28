import queue
from asyncio.windows_events import NULL
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # 取数组中间位置作为根节点的索引（偶数长度时取靠右的中间元素）
        m = len(nums) // 2
        left = self.sortedArrayToBST(nums[: m])
        right = self.sortedArrayToBST(nums[m+1: ])

        return TreeNode(nums[m], left, right)

    # 层序遍历
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        res = []

        # 队列不为空，继续处理
        while queue:    # while len(queue)>0:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res




if __name__ == "__main__":
    vals = [4,2,7,1,3,6,9]
    sol = Solution()