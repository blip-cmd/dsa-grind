class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # OPTIMIZATION / EARLY EXIT:
        # A valid bracket structure must have matching pairs.
        # If the string length is odd, at least one bracket is unmatched.
        if len(s) % 2 != 0:
            return False

        # DICTIONARY LOOKUP (O(1) Hash Map):
        # We key on CLOSING brackets so we can instantly check if an incoming 
        # character needs to resolve an existing open bracket.
        closing_to_opening_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        # THE STACK (LIFO structure):
        # Stores opening brackets waiting to be closed.
        bracket_stack = []

        for current_char in s:
            # CHECK IF CLOSING BRACKET:
            # In Python, 'key in dict' checks keys in O(1) time.
            if current_char in closing_to_opening_map:
                
                # TWO-PART SAFETY CHECK:
                # 1. 'bracket_stack': Ensures stack is non-empty before looking at index -1.
                #    Prevents IndexError if string starts with a closing bracket like "]".
                # 2. 'closing_to_opening_map[current_char] == bracket_stack[-1]':
                #    Checks if top of stack (last opened) matches expected opening bracket.
                if bracket_stack and closing_to_opening_map[current_char] == bracket_stack[-1]:
                    # Match confirmed! Pop top opening bracket off stack.
                    bracket_stack.pop()
                else:
                    # Either stack was empty (nothing to close) or 
                    # top bracket was wrong type (e.g., '(' matched with ']').
                    return False
            else:
                # IT'S AN OPENING BRACKET:
                # Push onto stack to await its matching closing bracket later.
                bracket_stack.append(current_char)

        # FINAL VERIFICATION:
        # If stack is empty (len == 0), all opening brackets were successfully matched.
        # If items remain (e.g., input was "(("), return False.
        return len(bracket_stack) == 0


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


times_solved = 2
# Difficulty: Easy
# https://leetcode.com/problems/valid-parentheses/
# key: stack, LIFO, matching pairs, early exit
# notes: Push opening brackets onto the stack. For each closing bracket, check for matching pair at the top of stack.
# Follow-up: 1. If non-bracket characters exist, ignore them (only push opening, only validate closing). 2. If memory is extremely constrained, mutating in place with counter pointers can work for depth but full nesting validation generally requires O(N) stack space.
# space: O(N). In the worst case, the stack stores every opening bracket from the input.
# time: O(N). Single pass through the string, and each bracket is pushed or popped at most once in O(1) time.
