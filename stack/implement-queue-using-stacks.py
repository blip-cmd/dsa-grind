class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # 1. If the processing stack is empty, pour everything from the input stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
        # 2. Pop and return the top element of the output stack
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """

        # 1. If the processing stack is empty, pour everything from the input stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
        # 2. Pop and return the top element of the output stack
        return self.out_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1, "Expected peek to return 1"
    assert q.pop() == 1, "Expected pop to return 1"
    assert not q.empty(), "Queue should not be empty"
    assert q.pop() == 2, "Expected pop to return 2"
    assert q.empty(), "Queue should be empty"
    print("All tests passed!")

# times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/implement-queue-using-stacks/
# key: Use two stacks (in_stack and out_stack) to reverse order for FIFO simulation.
# notes: Element transfer from in_stack to out_stack happens lazily when out_stack is empty.
# space: O(N) auxiliary space to store elements.
# time: O(1) amortized for pop and peek; O(1) worst-case for push and empty.
