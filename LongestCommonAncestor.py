'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
        	return(None)
        if root.val == p or root.val == q:
        	return(root)
        leftSearch = self.lowestCommonAncestor(root.left, p, q)
        rightSearch = self.lowestCommonAncestor(root.right, p, q)

        if leftSearch == None and rightSearch == None:
        	return(None)
        if leftSearch != None and rightSearch != None:
        	return(root)
        if leftSearch != None:
        	return(leftSearch)
        else:
        	return(rightSearch)

obj = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
#print((obj.lowestCommonAncestor(root, 5, 1)).val)
#print((obj.lowestCommonAncestor(root, 5, 4)).val)
print((obj.lowestCommonAncestor(root, 1, 2)).val)