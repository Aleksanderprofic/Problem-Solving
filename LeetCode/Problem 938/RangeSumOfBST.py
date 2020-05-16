class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is not None:
            sum = 0
            if root.val >= L:
                sum += self.rangeSumBST(root.left, L, R)
            if root.val <= R:
                sum += self.rangeSumBST(root.right, L, R)

            return sum
        return 0