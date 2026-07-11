# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0 
        def heightCalc(node): 
            if not node: 
                return 0 
            leftHeight = heightCalc(node.left)
            rightHeight = heightCalc(node.right)

            currentDiameter = leftHeight + rightHeight
            self.maxDia = max(self.maxDia,currentDiameter)
            return 1+max(leftHeight,rightHeight)
        heightCalc(root)
        return self.maxDia