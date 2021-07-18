'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
        	return True
        def iterate(root):
        	if root == None:
        		return 0
        	depth = max(iterate(root.left), iterate(root.right)) + 1
        	return depth
        result = abs(iterate(root.left) - iterate(root.right))
        if result <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        	return True
        else:
        	return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

obj = Solution()
print(obj.isBalanced(root))

'''
			1
		2 			2
	3					3
4   						4

def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        
        if not root:
            return True
        return abs(getDepth(root.left) - getDepth(root.right)) < =1 and \
                self.isBalanced(root.left) and self.isBalanced(root.right)
'''