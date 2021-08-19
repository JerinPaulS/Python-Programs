'''
Maximum Product of Splitted Binary Tree
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       	if root is None:
       		return 0
       	total_sum = [0]
       	max_prod = [0]
       	mod = (10 ** 9) + 7

       	def dfs_sum(root):
       		if root is None:
       			return
       		dfs_sum(root.left)
       		total_sum[0] = total_sum[0] + root.val
       		dfs_sum(root.right)
       		return

       	def dfs_find(root):
       		if root is None:
       			return 0
       		left_subtree = dfs_find(root.left)
       		right_subtree = dfs_find(root.right)
       		subtree_sum = left_subtree + right_subtree + root.val
       		prod = subtree_sum * (total_sum[0] - subtree_sum)
       		max_prod[0] = max(max_prod[0], prod)
       		return subtree_sum

       	dfs_sum(root)
       	dfs_find(root)
       	return max_prod[0] % mod

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

obj = Solution()
print(obj.maxProduct(root))       	