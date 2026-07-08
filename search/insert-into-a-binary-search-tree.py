# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)    
            
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

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

    # Test Case 1: root = [4,2,7,1,3], val = 5
    tree1 = build_tree_from_list([4, 2, 7, 1, 3])
    inserted1 = solution.insertIntoBST(tree1, 5)
    res1 = tree_to_list(inserted1)
    print("Test Case 1 after insertion:", res1)
    assert res1 == [4, 2, 7, 1, 3, 5]

    # Test Case 2: root = [40,20,60,10,30,50,70], val = 25
    tree2 = build_tree_from_list([40, 20, 60, 10, 30, 50, 70])
    inserted2 = solution.insertIntoBST(tree2, 25)
    res2 = tree_to_list(inserted2)
    print("Test Case 2 after insertion:", res2)
    assert res2 == [40, 20, 60, 10, 30, 50, 70, None, None, 25]


times_solved = 1
# Difficulty: Medium
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# key: recursion, binary search tree, insertion
# notes: Found the bugs in the initial implementation: (1) if root is None, we need to return the new node, and (2) when recursing left or right, we must assign the returned subtree back to root.left or root.right.
# space: O(H). Recursion stack height is H. In a balanced BST, H = O(log N). Worst case skewed tree is O(N).
# time: O(H). Traverse from root to leaf to insert. In a balanced BST, H = O(log N). Worst case skewed tree is O(N).
