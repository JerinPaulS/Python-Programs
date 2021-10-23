'''
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows - 1, -1, -1):
        	for col in range(cols - 1, -1, -1):
        		if row == rows - 1 and col == cols - 1:
        			continue
        		elif row == rows - 1:
        			grid[row][col] = grid[row][col] + grid[row][col + 1]
        		elif col == cols - 1:
        			grid[row][col] = grid[row][col] + grid[row + 1][col]
        		else:
        			grid[row][col] = grid[row][col] + min(grid[row][col + 1], grid[row + 1][col])
        return grid[0][0]