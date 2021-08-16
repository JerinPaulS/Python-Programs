'''
1260. Shift 2D Grid
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
'''
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        total_size = rows * cols
        flat_mat = []
        count = k % (rows * cols)

        for row in range(rows):
        	flat_mat.extend(grid[row])

        while count > 0:
        	flat_mat = [flat_mat[total_size - 1]] + flat_mat[:-1]
        	count = count - 1
        result = []
        start = 0
        end = cols
        for row in range(rows):
        	result.append(flat_mat[start:end])
        	start = start + cols
        	end = end + cols
        return result

obj = Solution()
print(obj.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(obj.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(obj.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))      