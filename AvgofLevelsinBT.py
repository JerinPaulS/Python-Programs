'''
637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if root is None:
        	return result
        que = deque()
        que.append(root)
        level_sum = 0
        while len(que) > 0:
        	level_sum = 0        	
        	level_size = len(que)
        	for node in range(level_size):
        		current_node = que.popleft()
        		level_sum = level_sum + current_node.val
        		if current_node.left is not None:
        			que.append(current_node.left)
        		if current_node.right is not None:
        			que.append(current_node.right)
        	result.append(level_sum / float(level_size))
        return result