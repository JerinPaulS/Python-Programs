'''
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        rotten_cordinates = []
        result = 0

        for row in range(rows):
        	for col in range(cols):
        		if grid[row][col] == 1:
        			fresh_count = fresh_count + 1
        		elif grid[row][col] == 2:
        			rotten_cordinates.append([row, col])
        if fresh_count == 0:
            return 0

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while len(rotten_cordinates) > 0:
        	size = len(rotten_cordinates)
        	result = result + 1
        	for index in range(size):
        		curr_x, curr_y = rotten_cordinates.pop(0)
        		print curr_x, curr_y, result
        		for d in directions:
        			new_x = curr_x + d[0]
        			new_y = curr_y + d[1]
        			if new_x < rows and new_x >= 0 and new_y >= 0 and new_y < cols and grid[new_x][new_y] == 1:
        				grid[new_x][new_y] = 2
        				fresh_count = fresh_count - 1
        				rotten_cordinates.append([new_x, new_y])

        if fresh_count == 0:
        	return result - 1
        else:
			return -1

obj = Solution()
print(obj.orangesRotting([[0,2]]))			