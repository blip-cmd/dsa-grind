# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l,r)+1
        
        #note: 1 recursive function with base case
        # keep in mind the naming conventions
        # time: as deep as tree is ish
        # space: 1


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: [3, 9, 20, None, None, 15, 7]
    tree1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    res1 = solution.maxDepth(tree1)
    print("Test Case 1 depth:", res1)
    assert res1 == 3

    # Test Case 2: [1, None, 2]
    tree2 = build_tree_from_list([1, None, 2])
    res2 = solution.maxDepth(tree2)
    print("Test Case 2 depth:", res2)
    assert res2 == 2

    # Test Case 3: Empty Tree
    tree3 = build_tree_from_list([])
    res3 = solution.maxDepth(tree3)
    print("Test Case 3 depth:", res3)
    assert res3 == 0


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# key: DFS, recursion, binary tree, post-order traversal
# notes: Recursively calculate the depth of the left and right subtrees. The max depth is 1 plus the maximum of the depths of the two subtrees.
# space: O(H). In the worst case of a skewed tree, O(N) stack frames; in the best case of a balanced tree, O(log N).
# time: O(N). Visits each node exactly once.
