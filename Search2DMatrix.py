'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1

        while top <= bot:
        	mid = (top + bot) // 2
        	if matrix[mid][-1] < target:
        		top = mid + 1
        	elif matrix[mid][0] > target:
        		bot = mid - 1
        	else:
        		break

        if not top <= bot:
        	return False

        start = 0
        end = cols - 1
        row = (top + bot) // 2
        while start <= end:
        	mid = (start + end) // 2
        	if matrix[row][mid] > target:
        		end = mid - 1
        	elif matrix[row][mid] < target:
        		start = mid + 1
        	else:
        		return True
        return False