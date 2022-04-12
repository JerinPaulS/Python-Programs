'''
289. Game of Life
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Original | New | State
        #    0    |  0  |   0
        #    1    |  0  |   1
        #    0    |  1  |   2
        #    1    |  1  |   3
        rows, cols = len(board), len(board[0])
        
        def countNeighbors(row, col):
            count = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (((i == row) and (j == col)) or i < 0 or j <0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1, 3]:
                        count += 1
                    elif board[i][j] == 1:
                        count += 1
            return count
        
        for row in range(rows):
            for col in range(cols):
                count = countNeighbors(row, col)
                if board[row][col] == 1:
                    if count in [2, 3]:
                        board[row][col] = 3
                    else:
                        board[row][col] = 1
                else:
                    if count == 3:
                        board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1
                    