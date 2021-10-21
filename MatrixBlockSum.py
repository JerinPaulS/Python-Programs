'''
1314. Matrix Block Sum
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''
class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        result = [[0] * cols for _ in range(rows)]

        for row in range(1, rows + 1):
        	for col in range(1, cols + 1):
        		dp[row][col] = mat[row - 1][col - 1] + dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1]

        for row in range(1, rows + 1):
        	for col in range(1, cols + 1):
        		start_row = max(1, row - k)
        		end_row = min(rows, row + k)
        		start_col = max(1, col - k)
        		end_col = min(cols, col + k)

        		result[row - 1][col - 1] = dp[end_row][end_col] - dp[start_row - 1][end_col] - dp[end_row][start_col - 1] + dp[start_row - 1][start_col - 1]

        return result