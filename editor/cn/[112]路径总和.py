# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。 
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
#          /  \      \
#         7    2      1
#  
# 
#  返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。 
#  Related Topics 树 深度优先搜索 
#  👍 429 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum_ == root.val
        return self.hasPathSum(root.left, sum_ - root.val) or self.hasPathSum(root.right, sum_ - root.val)
        # if not root:
        #     return False
        # stack = [(root, [root.val])]
        # while stack:
        #     node, tmp = stack.pop()
        #     # print(sum(tmp))
        #     if not node.left and not node.right and sum(tmp) == sum_:
        #         # print('ssada')
        #         return True
        #     if node.right:
        #         stack.append((node.right, tmp + [node.right.val]))
        #     if node.left:
        #         stack.append((node.left, tmp + [node.left.val]))
        # return False


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
    print(Solution().hasPathSum(root, -5))
