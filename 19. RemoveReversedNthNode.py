# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        if head.next is None:
            return None
        node_dict = {}
        index = 0  # index starts from 0
        while cur.next is not None:
            # find the last node
            node_dict[index] = cur
            index += 1
            cur = cur.next
        node_dict[index] = cur  # last index = length - 1

        length = index + 1
        removed = length - n  # removed node's index
        if removed == 0:  # remove first node
            return node_dict[1]
        elif removed == index:  # remove last node
            node_dict[removed-1].next = None
            return head
        else:
            node_dict[removed-1].next = node_dict[removed].next
            return head
