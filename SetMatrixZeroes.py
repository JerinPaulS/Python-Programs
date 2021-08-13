'''
Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r0 = 1
        rows  = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
        	for col in range(cols):
        		if matrix[row][col] == 0:
        			matrix[0][col] = 0
        			if row == 0:
        				r0 = 0
        			else:
        				matrix[row][0] = 0

        #print matrix, r0

        for row in range(1, rows):
        	for col in range(1, cols):
        		if matrix[0][col] == 0:
        			matrix[row][col] = 0
        		if row !=0 and matrix[row][0] == 0:
        			matrix[row][col] = 0

        if matrix[0][0] == 0:
        	for row in range(1, rows):
        		matrix[row][0] = 0

        if r0 == 0:
        	for col in range(cols):
        		matrix[0][col] = 0

        return matrix

obj = Solution()
print(obj.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(obj.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(obj.setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]))