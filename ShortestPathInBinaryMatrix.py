'''
1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] != 0:
            return -1
        
        def AdjacentNodes(node):
            i, j = node
            directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1)]
            result = []
            for row, col in directions:
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0:
                    result.append((row, col))
            return result

        targetNode = (len(grid) - 1, len(grid[0]) - 1)
        firstNodeDepth = ((0, 0), 1)
        queue = [firstNodeDepth]
        
        grid[0][0] = -1
        while len(queue) > 0:
            node, depth = queue.pop(0)
            
            if node == targetNode:
                return depth
    
            for adjNode in AdjacentNodes(node):
                grid[adjNode[0]][adjNode[1]] = -1
                queue.append((adjNode, depth + 1))
        return -1