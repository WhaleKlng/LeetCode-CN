# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
#  Related Topics 树 深度优先搜索 
#  👍 318 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            # print(stack)
            node, tmp = stack.pop()
            if not node.left and not node.right and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))
            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    # root = TreeNode(5)
    # root.left = TreeNode(4)
    # root.right = TreeNode(8)
    # root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)
    print(Solution().pathSum(root, -5))
