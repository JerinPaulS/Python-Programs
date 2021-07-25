'''
270. Closest Binary Search Tree Value
Description
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example
Example1


Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
'''
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        min_diff = target
        result = None
        while root is not None:
        	difference = abs(root.val - target)
        	if min_diff > difference:
        		min_diff = difference
        		result = root
        	if difference < root.val:
        		root = root.right
        	elif difference > root.val:
        		root = root.left
        	else:
        		return root.val
        return result.val



root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.right.left = TreeNode(8)
root.right.right = TreeNode(10)
root.left.left = TreeNode(2)

obj = Solution()
print(obj.closestValue(root, 4.142857))