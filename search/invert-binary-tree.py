# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
            
        return root


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


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Strip trailing Nones to match standard list representation
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: [4, 2, 7, 1, 3, 6, 9] -> [4, 7, 2, 9, 6, 3, 1]
    tree1 = build_tree_from_list([4, 2, 7, 1, 3, 6, 9])
    inverted1 = solution.invertTree(tree1)
    res1 = tree_to_list(inverted1)
    print("Test Case 1 inverted:", res1)
    assert res1 == [4, 7, 2, 9, 6, 3, 1]

    # Test Case 2: [2, 1, 3] -> [2, 3, 1]
    tree2 = build_tree_from_list([2, 1, 3])
    inverted2 = solution.invertTree(tree2)
    res2 = tree_to_list(inverted2)
    print("Test Case 2 inverted:", res2)
    assert res2 == [2, 3, 1]

    # Test Case 3: [] -> []
    tree3 = build_tree_from_list([])
    inverted3 = solution.invertTree(tree3)
    res3 = tree_to_list(inverted3)
    print("Test Case 3 inverted:", res3)
    assert res3 == []


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/invert-binary-tree/
# key: recursion, binary tree, post-order traversal, DFS
# notes: Swap the left and right child of each node, then recursively invert the left and right subtrees.
# space: O(H). Memory overhead on call stack is proportional to tree height H (worst case O(N), balanced O(log N)).
# time: O(N). Each node is visited exactly once.
