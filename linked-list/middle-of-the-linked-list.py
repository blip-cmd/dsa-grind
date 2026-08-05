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
        
        slow_runner,fast_runner = head,head

        while fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next #2x
        
        return slow_runner


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


# times_solved = 2
# Difficulty: Easy
# https://leetcode.com/problems/middle-of-the-linked-list/
# key: slow runner, fast runner, two pointers
# notes: Advance fast_runner 2x faster than slow_runner; when fast_runner hits the end, slow_runner points to the middle node.
# space: O(1). Uses only two pointer variables regardless of list length.
# time: O(N). Linear scan where fast_runner traverses the list in N/2 steps.
