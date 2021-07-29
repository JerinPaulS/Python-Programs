'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = []
        que = []
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
        	for col in range(cols):
        		if mat[row][col] == 0:
        			que.append((row, col))
        			visited.append((row, col))

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while len(que) > 0:
            curr_loc = que.pop(0)
            curr_row = curr_loc[0]
            curr_col = curr_loc[1]
            for i, j in directions:
                x = curr_row
                y = curr_col
                if x + i < rows and x + i >= 0 and y + j < cols and y + j >= 0 and (x + i, y + j) not in visited:
                    mat[x + i][y + j] = mat[x][y] + 1
                    visited.append((x + i, y + j))
                    que.append((x + i, y + j))

        return mat

obj = Solution()
print(obj.updateMatrix([[0,1,0,1,1],
						[1,1,0,0,1],
						[0,0,0,1,0],
						[1,0,1,1,1],
						[1,0,0,0,1]]))
'''						[[0,1,0,1,2],
						[1,1,0,0,1],
						[0,0,0,1,0],
						[1,0,1,1,1],
						[1,0,0,0,1]]
'''						

'''
		rows = len(mat)
		cols = len(mat[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if not mat[row][col]:
                    q.append((row, col))
                else:
                    mat[row][col] = float('inf')
        while len(q) > 0:
            row, col = q.popleft()
            dist = mat[row][col] + 1
            for nrow, ncol in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= nrow and nrow < rows and 0 <= ncol and ncol < cols and mat[nrow][ncol] > dist:
                    mat[nrow][ncol] = dist
                    q.append((nrow, ncol))
        return mat
'''