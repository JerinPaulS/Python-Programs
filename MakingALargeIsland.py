'''
Making A Large Island
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        parents = list(range(m * n))
        area = [1] * (m * n)

        def find(index):
        	if parents[index] != index:
        		parents[index] = find(parents[index])
        	return parents[index]

        def union(index1, index2):
        	root1 = find(index1)
        	root2 = find(index2)

        	if root1 != root2:
        		parents[root2] = root1
        		area[root1] = area[root1] + area[root2]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for x in range(m):
        	for y in range(n):
        		if grid[x][y] == 1:
        			for d in([[0, -1], [-1, 0]]):
        				new_x = x + d[0]
        				new_y = y + d[1]
        				if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
        					union(x * m + y, new_x * m + new_y)

        result = 0
        has_zero = False

        for x in range(m):
        	for y in range(n):
        		if grid[x][y] == 0:
        			visited = []
        			temp = 0
        			has_zero = True
        			for d in directions:
        				new_x = x + d[0]
        				new_y = y + d[1]

        				if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
        					index = new_x * m + new_y
        					root = find(index)
        					if root not in visited:
        						visited.append(root)
        						temp = temp + area[root]
        			result = max(result, temp)
        if has_zero:
        	return result + 1
        else:
        	return m * n

obj = Solution()
print(obj.largestIsland([[1,1],[1,0]]))       