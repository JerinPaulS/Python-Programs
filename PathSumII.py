'''
Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	def pathSum(self, root, targetSum):
		"""
		:type root: TreeNode
		:type targetSum: int
		:rtype: List[List[int]]
		"""
		result = []
		current = []

		def dfs(root, target, current):
			if root is None:
				return False
			current.append(root.val)
			if root.left is None and root.right is None:
				if target == root.val:
					result.append(current)
					return True
			dfs(root.left, target - root.val, current[:])
			dfs(root.right, target - root.val, current[:])
			return

		dfs(root, targetSum, current)
		return result

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

obj = Solution()
print(obj.pathSum(root, 22))