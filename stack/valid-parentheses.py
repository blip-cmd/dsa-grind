class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        lifo = []

        # opening = ['[','{','(']
        mapping = {']': '[', '}': '{', ')': '('}
        for a in s:
            c = str(a)
            if c in mapping:  # it's a close
                top_element = lifo.pop() if lifo else '#'

                if mapping[c] != top_element:
                    return False
            else:
                lifo.append(c)

        return len(lifo) == 0


if __name__ == "__main__":
    solution = Solution()

    result = solution.isValid("()")
    print(result)
    assert result is True

    result = solution.isValid("()[]{}")
    print(result)
    assert result is True

    result = solution.isValid("(]")
    print(result)
    assert result is False

    result = solution.isValid("([])")
    print(result)
    assert result is True

    result = solution.isValid("([)]")
    print(result)
    assert result is False

    result = solution.isValid("(")
    print(result)
    assert result is False


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/
# key: stack, LIFO, matching pairs
# notes: Push opening brackets onto the stack. For each closing bracket, the latest opening bracket must match its mapped pair.
# space: O(N). In the worst case, the stack stores every opening bracket from the input.
# time: O(N). The string is scanned once, and each bracket is pushed or popped at most once.
