# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if not root:
            return True
        
        return self.look(root.left,root.right)
        
    def look(self, left, right):
        if not left and not right: #none exist
            return True
        if not left or not right: #one exists
            return False
        return (left.val==right.val) and self.look(left.left,right.right) and self.look(left.right, right.left)


# Local helper class and test setup for local verification
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Test case 1: Symmetric tree [1,2,2,3,4,4,3]
    #      1
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    
    sol = Solution()
    assert sol.isSymmetric(root1) == True, "Test case 1 failed"
    
    # Test case 2: Asymmetric tree [1,2,2,None,3,None,3]
    #      1
    #    /   \
    #   2     2
    #    \     \
    #     3     3
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    assert sol.isSymmetric(root2) == False, "Test case 2 failed"
    
    print("All tests passed successfully!")

# times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/symmetric-tree/
# key: recursion, mirror properties (left.left == right.right and left.right == right.left)
# notes: Refactored to senior style. Helper method is private (_is_mirror) and clean split.
# space: O(H) recursion stack space where H is the height of the tree.
# time: O(N) where N is the number of nodes, visiting each node exactly once.
