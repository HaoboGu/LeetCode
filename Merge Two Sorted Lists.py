class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = []
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None:
                list.append(l2.val)
                l2 = l2.next
            elif l2 is None:
                list.append(l1.val)
                l1 = l1.next
            elif l1.val > l2.val:
                list.append(l2.val)
                l2 = l2.next
            else:
                list.append(l1.val)
                l1 = l1.next
        if list:
            return list
        else:
            return []



