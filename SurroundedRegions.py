'''
130. Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        stalled = set()
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in stalled or board[row][col] == "X":
                return
            stalled.add((row, col))
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    if (row, col) not in stalled:
                        dfs(row, col)
        for row in range(rows):
            for col in range(cols):
                  if board[row][col] == "O" and (row, col) not in stalled:
                        board[row][col] = "X"
        return board