# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


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


def linked_list_to_list(head):
    values = []
    node = head

    while node:
        values.append(node.val)
        node = node.next

    return values


if __name__ == "__main__":
    solution = Solution()

    head = build_linked_list([1, 2, 3, 4, 5])
    result = linked_list_to_list(solution.middleNode(head))
    print(result)
    assert result == [3, 4, 5]

    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = linked_list_to_list(solution.middleNode(head))
    print(result)
    assert result == [4, 5, 6]

    head = build_linked_list([1])
    result = linked_list_to_list(solution.middleNode(head))
    print(result)
    assert result == [1]


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/middle-of-the-linked-list/
# key: slow pointer, fast pointer, two pointers
# notes: Move `fast` two steps and `slow` one step; when `fast` reaches the end, `slow` is at the middle.
# space: O(1). Only two pointers are used, regardless of the linked list length.
# time: O(N). The fast pointer walks through the list once, so the traversal grows linearly with the number of nodes.
