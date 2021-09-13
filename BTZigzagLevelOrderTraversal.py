'''
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
        	return result

        que = [root]
        result.append([root.val])
        flag = 0

        while len(que) > 0:
        	temp = []
        	size = len(que)
        	while size > 0:
        		curr = que.pop(0)
        		if curr.left is not None:
        			que.append(curr.left)
        			temp.append(curr.left.val)
        		if curr.right is not None:
        			que.append(curr.right)
        			temp.append(curr.right.val)
        		size = size - 1
        	if flag and len(que) > 0:
        		result.append(temp)
        		flag = 0
        	elif not flag and len(que) > 0:
        		result.append(temp[::-1])
        		flag = 1

        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(4)
root.right.right = TreeNode(5)