# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def plus_two(x, y):
    """
    :param x: First number
    :param y: Second number
    :return: [carrier, result]
    """
    if x + y >= 10:
        return 1, (x+y) % 10
    else:
        return 0, x+y


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_l1 = l1
        cur_l2 = l2
        carrier, re = plus_two(cur_l1.val, cur_l2.val)
        new_root = ListNode(re)
        cur_node = new_root
        while cur_l1.next is not None and cur_l2.next is not None:
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            carrier, re = plus_two(cur_l1.val+carrier, cur_l2.val)
            new_node = ListNode(re)
            cur_node.next = new_node
            cur_node = new_node

        while cur_l1.next is not None:
            cur_l1 = cur_l1.next
            carrier, re = plus_two(cur_l1.val, carrier)
            new_node = ListNode(re)
            cur_node.next = new_node
            cur_node = new_node

        while cur_l2.next is not None:
            cur_l2 = cur_l2.next
            carrier, re = plus_two(cur_l2.val, carrier)
            new_node = ListNode(re)
            cur_node.next = new_node
            cur_node = new_node

        if carrier == 1:
            new_node = ListNode(1)
            cur_node.next = new_node
            cur_node = new_node
        return new_root
