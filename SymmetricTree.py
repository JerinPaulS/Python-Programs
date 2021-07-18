'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
        	return(self.check(root.left, root.right))
        else:
        	return(False)

    def check(self, left_tree, right_tree):
    	if left_tree is None and right_tree is None:
    		return(True)
    	if left_tree is None or right_tree is None:
    		return(False)
    	return((left_tree.val == right_tree.val) and self.check(left_tree.left, right_tree.right) and self.check(left_tree.right, right_tree.left))

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)        
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(2)

print(obj.isSymmetric(root))