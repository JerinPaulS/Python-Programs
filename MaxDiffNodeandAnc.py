'''
Maximum difference between node and its ancestor
Given a Binary Tree, you need to find the maximum value which you can get by subtracting the value of node B from the value of node A, where A and B are two nodes of the binary tree and A is an ancestor of B. 

Example 1:

Input:
    5
 /    \
2      1
Output: 4
Explanation:The maximum difference we can
get is 4, which is bewteen 5 and 1.
Example 2:

Input:
      1
    /    \
   2      3
           \
            7
Output: -1
Explanation:The maximum difference we can
get is -1, which is between 1 and 2.
Your Task:
The task is to complete the function maxDiff() which finds the maximum difference between the node and its ancestor.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree.

Constraints:
1 <= Number of edges <= 104
0 <= Data of a node <= 105
'''
#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return the maximum difference between any node and its ancestor.
def maxDiff(root):
   
    # code here
    max_node = [float('-inf')]
    result = [float('-inf')]
    def dfs(node):
    	if node is None:
    		return
    	result[0] = max(result[0], max_node[0] - node.data)
    	max_node[0] = max(max_node[0], node.data)
    	dfs(node.left)
    	dfs(node.right)

    dfs(root)
    return result[0]