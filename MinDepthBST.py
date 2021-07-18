'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None:
            return 0
        left_depth = self.minDepth(root.left) + 1
        right_depth = self.minDepth(root.right) + 1
        if left_depth > 1 and right_depth > 1:
            return min(left_depth, right_depth)
        elif left_depth == 1:
            return right_depth
        elif right_depth == 1:
            return left_depth


root = TreeNode(3)
root.right = TreeNode(9)
root.left = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

obj = Solution()
print(obj.minDepth(root))
'''
							-9
				-3							2
					4				4			0
				-6						-5



'''