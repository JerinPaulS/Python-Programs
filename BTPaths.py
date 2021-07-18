'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def calc(root, result, res_str):
            res_str = res_str + "->" + str(root.val)
            if root.left is None and root.right is None:
                result.append(res_str)
                return
            if root.right is not None:
                calc(root.right, result, res_str)
            if root.left is not None:
                calc(root.left, result, res_str)

        result = []
        if root is None:
            return result
        res_str = str(root.val)
        if root.left is None and root.right is None:
            result.append(res_str)
            return result
        if root.left is not None:
            calc(root.left, result, res_str)
        if root.right is not None:
            calc(root.right, result, res_str)
        return result