# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current_node = head
        ans = 0

        while current_node:
            ans = (ans << 1) | current_node.val
            current_node = current_node.next
        return ans


def simulate_shift():
    print("--- Linked List Binary Shifting Simulator ---")
    binary_str = input("Enter a binary number (e.g., 101): ").strip()

    ans = 0
    print(f"\nStarting with ans = {ans} (Binary: {ans:04b})")

    for i, bit_char in enumerate(binary_str):
        bit = int(bit_char)
        print(f"\n--- Node {i + 1}: Node value is {bit} ---")

        shifted_ans = ans << 1
        print(
            f"1. Shift left (ans << 1): {ans} becomes {shifted_ans} "
            f"(Binary: {shifted_ans:04b})"
        )

        ans = shifted_ans | bit
        print(
            f"2. Add node value (ans | {bit}): Final ans is {ans} "
            f"(Binary: {ans:04b})"
        )

    print(f"\nFinal Decimal Value: {ans}")


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


if __name__ == "__main__":
    test_cases = [
        ([1, 0, 1], 5),
        ([0], 0),
        ([1], 1),
        ([1, 0, 0, 1], 9),
        ([1, 1, 1, 1], 15),
    ]

    solution = Solution()

    for values, expected in test_cases:
        head = build_linked_list(values)
        result = solution.getDecimalValue(head)
        print(f"{values} -> {result} | expected: {expected}")
        assert result == expected

    # Uncomment this when you want to review the bit-shift process step by step.
    # simulate_shift()


times_solved = 2

# Difficulty: Easy
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# notes: bit manipulation, <<, singly-linked list
# Key: The main idea is to traverse the linked list and for each node, shift the current answer to the left (multiply by 2) and then add the node's value (0 or 1). This effectively builds the binary number as we go through the list.
# Complexity Analysis (Interview-Ready Summary)
# Time Complexity: O(N), where N is the number of nodes in the linked list. We visit each node exactly once.
# Space Complexity: O(1) auxiliary space. We only use two variables, current_node and ans, no matter how long the list is.
