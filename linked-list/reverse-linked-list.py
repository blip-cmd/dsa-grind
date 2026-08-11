# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #loop over all nodes and repoint
        current_node=head
        previous_node = None

        while current_node:
            upcoming_node = current_node.next
            current_node.next =  previous_node 

            previous_node = current_node
            current_node = upcoming_node
            
        return previous_node


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
    result = linked_list_to_list(solution.reverseList(head))
    print(result)
    assert result == [5, 4, 3, 2, 1]

    head = build_linked_list([1, 2])
    result = linked_list_to_list(solution.reverseList(head))
    print(result)
    assert result == [2, 1]

    head = build_linked_list([])
    result = linked_list_to_list(solution.reverseList(head))
    print(result)
    assert result == []


# times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/reverse-linked-list/
# key: iterative, pointer manipulation
# notes: Loop through the list, keep track of current, previous, and next nodes, and reverse pointers in-place.
# space: O(1). Uses only a few pointers for iteration and reversal.
# time: O(N). Traverses the entire linked list of N nodes once.

#TODO: try recursive approach