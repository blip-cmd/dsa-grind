class MinStack(object):

    def __init__(self):
        self._min = []
        self._main = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        # my inital mistake
        # self._min.append(value) if value < self._min[-1] else self._min.append(self._min[-1]) if self.min[-1]
        # self._main.append(value)

        # If min_stack is empty, or val is less/equal to current min
        if not self._min or value <= self._min[-1]:
            self._min.append(value)
        else:
            self._min.append(self._min[-1])

        self._main.append(value)

        return None
        

    def pop(self):
        """
        :rtype: None
        """
        self._min.pop()
        return self._main.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._main[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[-1]
        

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
    print("All tests passed!")


times_solved = 2
# Difficulty: Medium
# https://leetcode.com/problems/min-stack/
# key: design, stack, min-tracking
# notes: Maintain a secondary stack to track the minimum element up to each depth level of the main stack.
# space: O(N). The space complexity is O(N) because we maintain a main stack and a minimum stack, each holding up to N elements.
# time: O(1). All operations (push, pop, top, getMin) take constant time because we only perform list appends, pops, and indexing.
