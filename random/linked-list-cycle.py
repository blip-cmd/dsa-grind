# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Thanks to Floyd's approach
        slow,fast  = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow: #is checks if two objects are in the same memory slot.
                return True

        return False
        