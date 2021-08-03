'''
783. Minimum Distance Between BST Nodes
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
 

Note: This question is the same as 530:
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_val = []
        result = 10 ** 5

        def dfs_inorder(root):
            if root is None:
                return None
            dfs_inorder(root.left)
            node_val.append(root.val)
            dfs_inorder(root.right)
            return
        dfs_inorder(root)

        for index in range(len(node_val) - 1):
            result = min(result, abs(node_val[index + 1] - node_val[index]))

        return result