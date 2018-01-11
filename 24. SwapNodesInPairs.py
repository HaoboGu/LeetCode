# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        cur = head
        new_head = head.next
        while cur.next is not None:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = cur
            cur = cur.next
        return new_head
