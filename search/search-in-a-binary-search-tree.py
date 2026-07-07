# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.val == val:
            return root
       
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


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

    # Test Case 1: root = [4,2,7,1,3], val = 2 -> [2,1,3]
    tree1 = build_tree_from_list([4, 2, 7, 1, 3])
    found1 = solution.searchBST(tree1, 2)
    res1 = tree_to_list(found1)
    print("Test Case 1 found subtree:", res1)
    assert res1 == [2, 1, 3]

    # Test Case 2: root = [4,2,7,1,3], val = 5 -> []
    tree2 = build_tree_from_list([4, 2, 7, 1, 3])
    found2 = solution.searchBST(tree2, 5)
    res2 = tree_to_list(found2)
    print("Test Case 2 found subtree:", res2)
    assert res2 == []


times_solved = 1
# Difficulty: Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# key: recursion, binary search tree, search
# notes: Base cases are if root is None or if root.val matches. Otherwise, traverse left if val < root.val, or right if val > root.val.
# space: O(H). Recursion stack height is H. In a balanced BST, H = O(log N). Worst case skewed tree is O(N).
# time: O(H). In a balanced BST, H = O(log N). Worst case skewed tree is O(N).
