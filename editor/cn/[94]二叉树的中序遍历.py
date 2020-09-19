# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 714 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = []
        node = root
        while node or stack:  # 当节点不为空或者栈中还有东西的时候
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()  # 左子树的根节点都进来了 + 最左叶子节点
            ans.append(node.val)
            node = node.right
        return ans

# leetcode submit region end(Prohibit modification and deletion)
