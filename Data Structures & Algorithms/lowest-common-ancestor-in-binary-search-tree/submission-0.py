class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Safely extract values in case p or q are passed as objects or ints
        p_val = p.val if hasattr(p, 'val') else p
        q_val = q.val if hasattr(q, 'val') else q
        
        # Base Case: Compare node values instead of raw memory addresses
        if not root or root.val == p_val or root.val == q_val:
            return root
            
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result and right_result:
            return root
            
        return left_result if left_result else right_result