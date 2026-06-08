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
        ans = 0

        while head:
            ans = (ans << 1) | head.val
            head = head.next

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


if __name__ == "__main__":
    # simulate_shift()


times_solved = 1
