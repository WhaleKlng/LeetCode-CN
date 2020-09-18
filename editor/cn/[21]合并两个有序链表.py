# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1238 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # while l1 or l2:
        #     if l1.val < l2.val:
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #         return l1
        #     else:
        #         l2.next = self.mergeTwoLists(l1, l2.next)
        #         return l2
        node = ListNode(-1)
        p = node
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 else l2

            # print(p.val)
        return node.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # 1->2->4, 1->3->4
    node1 = ListNode(1)
    node1.next = ListNode(3)
    node1.next.next = ListNode(5)
    node2 = ListNode(8)
    node2.next = ListNode(11)
    node2.next.next = ListNode(33)
    root = Solution().mergeTwoLists(node1, node2)
    while root:
        print(root.val)
        root = root.next
