# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        # dummy node
        sentinel = ListNode()    #create
        sentinel.next = head    #point

        #iterate
        node = sentinel #tracker
        while node.next: #bounds
            if node.next.val == val: #same val?
                node.next = node.next.next # skip middle & point left to right
            else:
                node = node.next # if dif val, update tracker

        #return
        return sentinel.next


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

    head = build_linked_list([1, 2, 6, 3, 4, 5, 6])
    result = linked_list_to_list(solution.removeElements(head, 6))
    print(result)
    assert result == [1, 2, 3, 4, 5]

    head = build_linked_list([])
    result = linked_list_to_list(solution.removeElements(head, 1))
    print(result)
    assert result == []

    head = build_linked_list([7, 7, 7, 7])
    result = linked_list_to_list(solution.removeElements(head, 7))
    print(result)
    assert result == []


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/remove-linked-list-elements/
# key: dummy node, previous pointer, linked list deletion
# notes: Use sentinel so deleting the head is handled the same way as deleting any middle node.
# space: O(1). You only allocate one sentinel node and one tracking pointer (`node`), independent of input size.
# time: O(N). You traverse the list exactly once; every node is inspected at most twice, once via `node.next` and once via `node`.
