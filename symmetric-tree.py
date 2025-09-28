# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                self.isMirror(t1.left, t2.right) and 
                self.isMirror(t1.right, t2.left))

# -------------------------
# Build Tree 1 (symmetric)
#       1
#      / \
#     2   2
#    /     \
#   3       3
tree1 = TreeNode(1)
tree1.left = TreeNode(2, TreeNode(3))
tree1.right = TreeNode(2, None, TreeNode(3))

# Build Tree 2 (symmetric)
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
tree2 = TreeNode(1)
tree2.left = TreeNode(2, TreeNode(3), TreeNode(4))
tree2.right = TreeNode(2, TreeNode(4), TreeNode(3))

# -------------------------
# Test
sol = Solution()
print(sol.isSymmetric(tree1))  # True
print(sol.isSymmetric(tree2))  # True
