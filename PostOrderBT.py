'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [2,1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
        	return result
        stack1 = []
        stack2 = []
        stack1.append(root)
        while len(stack1) > 0:
        	root = stack1.pop()
        	stack2.append(root)
        	if root.left is not None:
        		stack1.append(root.left)
        	if root.right is not None:
        		stack1.append(root.right)
        	
        while len(stack2) > 0:
        	result.append(stack2.pop().val)
        return result


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
#root.right.left = TreeNode(3)

obj = Solution()
print(obj.postorderTraversal(root))