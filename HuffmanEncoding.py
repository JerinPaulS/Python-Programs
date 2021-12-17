'''
Huffman Encoding
Given a string S of distinct character of size N and their corresponding frequency f[ ] i.e. character S[i] has f[i] frequency. Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree.
Note: If two elements have same frequency, then the element which occur at first will be taken on the left of Binary Tree and other one to the right.

Example 1:

S = "abcdef"
f[] = {5, 9, 12, 13, 16, 45}
Output: 
0 100 101 1100 1101 111
Explanation:
HuffmanCodes will be:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111
Hence printing them in the PreOrder of Binary 
Tree.
Your Task:
You don't need to read or print anything. Your task is to complete the function huffmanCodes() which takes the given string S, frequency array f[ ] and number of characters N as input parameters and returns a vector of strings containing all huffman codes in order of preorder traversal of the tree.

Expected Time complexity: O(N * LogN) 
Expected Space complexity: O(N) 

Constraints:
1 ≤ N ≤ 26
'''
class Tree:
	def __init__(self, val, freq):
		self.val = val
		self.freq = freq
		self.left = None
		self.right = None

import heapq
import collections
class Solution:
    def huffmanCodes(self,S,f,N):
    	freq_dict = collections.defaultdict(str)
    	heap = []
    	visited = {}
    	head = Tree(" ", -1)
    	for index, val in enumerate(f):
    		heapq.heappush(heap, val)
    		freq_dict[val] = S[index]

    	while len(heap) > 1:
    		t1 = heapq.heappop(heap)
    		t2 = heapq.heappop(heap)
    		if t1 in visited:
    			left = visited[t1]
    			visited.pop(t1)
    		else:
    			left = Tree(freq_dict[t1], t1)
    		if t2 in visited:
    			right = visited[t2]
    			visited.pop(t2)
    		else:
    			right = Tree(freq_dict[t2], t2)
    		node = Tree("11", t1 + t2)
    		head.left = node
    		visited[t1 + t2] = node
    		node.left = left
    		node.right = right
    		heapq.heappush(heap, t1 + t2)
    	result = {}
    	def dfs(node, curr):
    		if node is None:
    			return
    		if node.left is None and node.right is None:
    			result[node.val] = curr
    			return
    		dfs(node.left, curr[:] + "0")
    		dfs(node.right, curr[:] + "1")
    	
    	dfs(head.left, "")
    	out = []

    	def preorder(node):
    		if node is None:
    			return
    		out.append(node.val)
    		preorder(node.left)
    		preorder(node.right)

    	res = []
    	preorder(head.left)
    	for v in out:
    		if v == "11":
    			continue
    		res.append(result[v])
    	return res
    	

obj = Solution()
print(obj.huffmanCodes("abcdef", [5, 9, 12, 13, 16, 45], 6))