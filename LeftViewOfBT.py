'''
Left View of Binary Tree
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Example 2:

Input:

Output: 10 20 40
Your Task:
You just have to complete the function leftView() that prints the left view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000
'''
#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
import collections
def LeftView(root):
	level_dict = {}

	def dfs(node, level, depth):
		if node is None:
			return
		dfs(node.left, level - 1, depth + 1)
		if level_dict.has_key(depth):
			if level_dict[depth][0] > level:
				level_dict[depth] = [level, node.data]
		else:
			level_dict[depth] = [level, node.data]
		dfs(node.right, level + 1, depth + 1)

	dfs(root, 0, 0)
	result = []
	for key in level_dict.keys():
		result.append(level_dict[key][1])
	return result