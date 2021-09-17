'''
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

'''
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		rows, cols = len(obstacleGrid), len(obstacleGrid[0])
		if obstacleGrid[rows - 1][cols - 1] or obstacleGrid[0][0]:
			return 0

		for row in range(1, rows):
			if row > 0 and row < rows - 1:
				if sum(obstacleGrid[row]) == cols:
					return 0
			for col in range(1, cols):
				if obstacleGrid[row][col] == 1:
					obstacleGrid[row][col] = 0
				else:
					obstacleGrid[row][col] = 1
		flag = 0
		for col in range(1, cols):
			if flag:
				obstacleGrid[0][col] = 0
				continue
			if obstacleGrid[0][col] == 1:
				flag = 1
				obstacleGrid[0][col] = 0
			else:
				obstacleGrid[0][col] = 1
		flag = 0
		for row in range(rows):
			if flag:
				obstacleGrid[row][0] = 0
				continue
			if obstacleGrid[row][0] == 1:
				flag = 1
				obstacleGrid[row][0] = 0
			else:
				obstacleGrid[row][0] = 1

		for row in range(1, rows):
			for col in range(1, cols):
				if obstacleGrid[row][col] != 0:
					obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]

		return obstacleGrid[-1][-1]


obj = Solution()
print(obj.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

'''
[[0,0,0],[0,1,0],[0,0,0]]
[[0,1],[0,0]]
[[0,0],[0,1]]
[[1,0],[0,0]]
[[0,1],[1,0]]
[[0,0],[0,0],[1,1],[0,0]]
[[0,0],[1,1],[0,0]]
[[1,1],[0,0],[0,0]]
[[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]]
[[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
'''		