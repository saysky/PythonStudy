# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 删除重复元素，每个元素出现一次
class Solution:
    # 输入：head = [1, 1, 2]
    # 输出：[1, 2]

    # 输入：head = [1, 1, 2, 3, 3]
    # 输出：[1, 2, 3]
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        pre = head
        p = head.next
        while p:
            if pre.val == p.val:
                pre.next = p.next
                p = pre.next
            else:
                pre = p
                p = p.next
        return head
