'''
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
        	return 0
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        result = 0

        def dfs(row, col):
        	stack = [(row, col)]
        	while len(stack) > 0:
        		row, col = stack.pop()
        		for d in direction:
        			new_x, new_y = row + d[0], col + d[1]
        			if new_x >= 0 and new_x < rows and new_y >=0 and new_y < cols:
        				if (new_x, new_y) not in visited and grid[new_x][new_y] == "1":
        					visited.add((new_x, new_y))
        					stack.append((new_x, new_y))
        	return

        for row in range(rows):
        	for col in range(cols):
        		if grid[row][col] == "1" and (row, col) not in visited:
        			visited.add((row, col))
        			result = result + 1
        			dfs(row, col)

        return result

obj = Solution()
print(obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))       