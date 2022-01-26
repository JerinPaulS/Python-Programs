'''
1305. All Elements in Two Binary Search Trees
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = []
        list2 = []
        result = []
        
        def dfs(node, curr):
            if node is None:
                return
            dfs(node.left, curr)
            curr.append(node.val)
            dfs(node.right, curr)
            return curr
        
        if root1 is not None:
            list1 = dfs(root1, [])
        if root2 is not None:
            list2 = dfs(root2, [])
        ptr1, ptr2 = 0, 0
        if len(list1) == 0:
            return list2
        if len(list2) == 0:
            return list1
        while ptr1 < len(list1) and ptr2 < len(list2):
            if list1[ptr1] < list2[ptr2]:
                result.append(list1[ptr1])
                ptr1 += 1
            else:
                result.append(list2[ptr2])
                ptr2 += 1
        while ptr1 < len(list1):
            result.append(list1[ptr1])
            ptr1 += 1
        while ptr2 < len(list2):
            result.append(list2[ptr2])
            ptr2 += 1
        return result