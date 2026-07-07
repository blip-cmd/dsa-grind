# Tree Properties & Complexity Reference

| Tree Type | Core Structural Rule | Best/Average Time Complexity | Worst-Case Time Complexity | Space Complexity (Call Stack) | Common Use Cases / Interview Patterns |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Binary Tree (General)** | Each node has at most two children (left and right). No rules about value placement. | $O(N)$ (Must visit all nodes) | $O(N)$ | $O(H)$ (Where $H$ is tree height) | Finding max depth, checking symmetry, flipping/inverting structure. |
| **Binary Search Tree (BST)** | Left subtree values < Parent. Right subtree values > Parent. | $O(\log N)$ (Halves search space at each step) | $O(N)$ (If tree becomes a straight line / skewed) | $O(H)$ ($O(\log N)$ balanced, $O(N)$ unbalanced) | Fast targeted searching, insertion, and sorting elements hierarchically. |
