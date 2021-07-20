'''
501. Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    prevNode = None
    result = []
    max_count = 0
    count = 1

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """			

        def dfs_inorder(root):
            if root is None:
                return
            dfs_inorder(root.left)

            if self.prevNode is not None:
                if root.val == self.prevNode.val:
                    self.count = self.count + 1
                else:
                    self.count = 1

            if self.max_count < self.count:
                self.max_count = self.count
                self.result = []
                if root.val not in self.result:
                    self.result.append(root.val)
            elif self.max_count == self.count:
                if root.val not in self.result:
                    self.result.append(root.val)

            self.prevNode = root

            dfs_inorder(root.right)
            return self.result		

        return dfs_inorder(root)

root = TreeNode(1)
#root.right = TreeNode(2)
#root.right.left = TreeNode(2)

obj = Solution()
print(obj.findMode(root))