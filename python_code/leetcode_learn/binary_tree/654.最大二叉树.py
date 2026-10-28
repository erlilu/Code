from platform import node
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        max_num = max(nums)
        root_idx = nums.index(max_num)
        root = TreeNode(val= max_num)

        root.left = self.constructMaximumBinaryTree(nums[: root_idx])
        root.right = self.constructMaximumBinaryTree(nums[root_idx + 1 :])

        return root
