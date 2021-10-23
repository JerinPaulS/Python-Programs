'''
221. Maximal Square
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def helper(row, col):
        	if row >= rows or col >= cols:
        		return 0

        	if (row, col) in cache:
        		return cache[(row, col)]

        	else:
        		down = helper(row + 1, col)
        		right = helper(row, col + 1)
        		diag = helper(row + 1, col + 1)

        		cache[(row, col)] = 0
        		if matrix[row][col] == "1":
        			cache[(row, col)] = 1 + min(down, right, diag)
        	return cache[(row, col)]

        helper(0, 0)
        return (max(cache.values()) ** 2)