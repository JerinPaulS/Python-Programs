'''
404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(node, side):
        	if node is None:
        		return
        	if node.left is None and node.right is None and side:
        		result[0] = result[0] + node.val
        		return
        	dfs(node.left, 1)
        	dfs(node.right, 0)

        dfs(node, 0)
        return result[0]