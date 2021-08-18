'''
1380. Lucky Numbers in a Matrix
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.

'''
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        min_row = []
        max_col = []

        for row in range(rows):
        	min_row.append(min(matrix[row]))

        for col in range(cols):
        	max_el = matrix[0][col]
        	for row in range(1, rows):
        		max_el = max(max_el, matrix[row][col])
        	max_col.append(max_el)

        print min_row, max_col

        for val in min_row:
        	if val in max_col:
        		return [val]

        return []

obj = Solution()
print(obj.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))