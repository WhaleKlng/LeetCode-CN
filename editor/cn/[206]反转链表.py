# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1211 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # 若链表为空或者仅一个数就直接返回
            return head
        pre = None
        next = None
        while (head != None):
            next = head.next  # 1 先存起来下一个节点
            head.next = pre  # 2 进行反转  当前节点的下一个指向继承来的上一个
            pre = head  # 3  更新 当前节点为pre  为下一轮的时候做备胎
            head = next  # 4 把head后移一位
        return pre


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(3)
    node1.next.next = ListNode(5)
    root = Solution().reverseList(node1)
    while root:
        print(root.val)
        root = root.next
