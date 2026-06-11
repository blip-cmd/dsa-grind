# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        lifo = [] # lifo list

        current = head # pointing finger
        while current: # 1st pass
            lifo.append(current.val) # store in lifo
            current = current.next

        current = head # reset
        while current: # 2nd pass
            if current.val != lifo.pop(): # check
                return False
            current = current.next

        return True


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    sentinel = ListNode()
    node = sentinel

    for value in values:
        node.next = ListNode(value)
        node = node.next

    return sentinel.next


if __name__ == "__main__":
    solution = Solution()

    head = build_linked_list([1, 2, 2, 1])
    result = solution.isPalindrome(head)
    print(result)
    assert result is True

    head = build_linked_list([1, 2])
    result = solution.isPalindrome(head)
    print(result)
    assert result is False

    head = build_linked_list([1, 2, 3, 2, 1])
    result = solution.isPalindrome(head)
    print(result)
    assert result is True

    head = build_linked_list([])
    result = solution.isPalindrome(head)
    print(result)
    assert result is True


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/palindrome-linked-list/
# key: stack, LIFO, two passes
# notes: Store the values in a stack, then walk the list again and compare each node to the values popped from the end.
# space: O(N). The stack stores one value for every node in the linked list.
# time: O(N). One pass fills the stack and one pass compares values, so the work grows linearly with the number of nodes.
