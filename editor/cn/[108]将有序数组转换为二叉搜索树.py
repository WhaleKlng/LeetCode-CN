# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。 
# 
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。 
# 
#  示例: 
# 
#  给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics 树 深度优先搜索 
#  👍 579 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid + 1:]

        # 开始递归
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node
# leetcode submit region end(Prohibit modification and deletion)
