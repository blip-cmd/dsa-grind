# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        results = [] 
        from collections import deque
        q = deque([root])

        while q:
            n = len(q)
            level_vals = []
            for _ in range(n):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            results.append(level_vals)
        
        return results[::-1]


# Local helper class & utilities for testing
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: root = [3,9,20,null,null,15,7]
    root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    res1 = sol.levelOrderBottom(root1)
    print("Test 1 Result:", res1)
    assert res1 == [[15, 7], [9, 20], [3]], "Failed Test 1"
    
    # Test case 2: root = [1]
    root2 = build_tree_from_list([1])
    res2 = sol.levelOrderBottom(root2)
    print("Test 2 Result:", res2)
    assert res2 == [[1]], "Failed Test 2"
    
    # Test case 3: root = []
    root3 = build_tree_from_list([])
    res3 = sol.levelOrderBottom(root3)
    print("Test 3 Result:", res3)
    assert res3 == [], "Failed Test 3"
    
    print("All tests passed!")

# times_solved = 1
# Difficulty: Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# key: BFS traversal with level-by-level tracking, reversed at the end
# notes: Process tree level-by-level (BFS) using a queue, then reverse the resulting list of levels to get bottom-up order.
# space: O(N) where N is the maximum width of the tree, which is O(N) in the worst case.
# time: O(N) as each node is visited and processed exactly once.
