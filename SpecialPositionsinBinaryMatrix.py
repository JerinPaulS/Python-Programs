'''
1582. Special Positions in a Binary Matrix
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 
Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2
Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3
 

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
'''
import collections
class Solution(object):
	def numSpecial(self, mat):
		"""
		:type mat: List[List[int]]
		:rtype: int
		"""
		r_size = len(mat)
		c_size = len(mat[0])
		rows = collections.defaultdict(int)
		cols = collections.defaultdict(int)

		index_list = []

		for row in range(r_size):
			for col in range(c_size):
				if mat[row][col] == 1:
					rows[row] = rows[row] + 1
					cols[col] = cols[col] + 1
					index_list.append((row, col))

		print rows
		print cols

		result = 0
		for row, col in index_list:
			if rows[row] == cols[col] == 1:
				print row, col
				result = result + 1
		return result

obj = Solution()
print(obj.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))