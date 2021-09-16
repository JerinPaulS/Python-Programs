'''
Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
        	for i in range(left, right):
        		result.append(matrix[top][i])
        	top = top + 1
        	for i in range(top, bottom):
        		result.append(matrix[i][right - 1])
        	right = right - 1
        	if not (left < right and top < bottom):
        		break
        	for i in range(right - 1, left - 1, -1):
        		result.append(matrix[bottom - 1][i])
        	bottom = bottom - 1
        	for i in range(bottom - 1, top - 1, -1):
        		result.append(matrix[i][left])
        	left = left + 1
        return result