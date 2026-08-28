class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {0: 0, 1: 1}

        def compute(x):
            if x in cache:
                return cache[x]

            result = compute(x - 1) + compute(x - 2)

            cache[x] = result
            return result

        return compute(n)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: n = 2 -> F(2) = F(1) + F(0) = 1 + 0 = 1
    assert sol.fib(2) == 1, "Test case 1 failed"

    # Test case 2: n = 3 -> F(3) = F(2) + F(1) = 1 + 1 = 2
    assert sol.fib(3) == 2, "Test case 2 failed"

    # Test case 3: n = 4 -> F(4) = F(3) + F(2) = 2 + 1 = 3
    assert sol.fib(4) == 3, "Test case 3 failed"

    # Test case 4: base cases n = 0, n = 1
    assert sol.fib(0) == 0, "Test case 4a failed"
    assert sol.fib(1) == 1, "Test case 4b failed"

    # Test case 5: larger n
    assert sol.fib(10) == 55, "Test case 5 failed"

    print("All tests passed successfully!")

# times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/fibonacci-number/
# key: Top-down Dynamic Programming (Memoization) with dictionary cache
# notes: Clean top-down recursive memoization approach avoiding exponential O(2^N) recalculations. Can also be optimized to O(1) space iteratively with two variables (bottom-up).
# space: O(N). Hash map cache storing N entries plus O(N) recursive call stack frames.
# time: O(N). Each state from 0 to N is computed at most once.
