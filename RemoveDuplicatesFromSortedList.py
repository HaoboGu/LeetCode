
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
        else:
            previous = head
            current = head.next
            while current != None:
                if current.val == previous.val:
                    previous.next = current.next
                    current = previous.next
                else:
                    previous = current
                    current = current.next
        return head

