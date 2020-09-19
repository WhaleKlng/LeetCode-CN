# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。 
# 
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。 
# 
#  示例: 
# 
#  给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics 深度优先搜索 链表 
#  👍 365 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# # Definition
# # for a binary tree node.
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next

        def helper(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            left = nums[:mid]
            right = nums[mid + 1:]

            node.left = helper(left)
            node.right = helper(right)

            return node

        return helper(ans)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    linnode = ListNode(1)
    linnode.next = ListNode(2)
    linnode.next.next = ListNode(3)
    linnode.next.next.next = ListNode(4)
    linnode.next.next.next.next = ListNode(5)
    linnode.next.next.next.next.next = ListNode(6)
    linnode.next.next.next.next.next.next = ListNode(7)
    linnode.next.next.next.next.next.next.next = ListNode(8)
    print(Solution().sortedListToBST(linnode))
