'''
999. Available Captures for Rook
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

 

Example 1:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
Example 2:


Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.
Example 3:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
 

Constraints:

board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
'''
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = 8
        cols = 8

        current = []
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for row in range(rows):
        	for col in range(cols):
        		if board[row][col] == "R":
        			current.append(row)
        			current.append(col)
        			break
        	if len(current) > 0:
        		break

        flag_North = 0
        flag_East = 0
        flag_South = 0
        flag_West = 0
        curr_x = current[0]
        curr_y = current[1]
        N = [curr_x, curr_y]
        E = [curr_x, curr_y]
        S = [curr_x, curr_y]
        W = [curr_x, curr_y]

        result = 0

        while flag_North == 0 or flag_East == 0 or flag_South == 0 or flag_West == 0:
        	N[0], N[1] = N[0] + directions[0][0], N[1] + directions[0][1]
        	E[0], E[1] = E[0] + directions[1][0], E[1] + directions[1][1] 
        	S[0], S[1] = S[0] + directions[2][0], S[1] + directions[2][1] 
        	W[0], W[1] = W[0] + directions[3][0], W[1] + directions[3][1]

        	if flag_North == 0 and N[0] >= 0:
        		if board[N[0]][N[1]] == "B":
        			flag_North = 1
        		elif board[N[0]][N[1]] == "p":
        			result = result + 1
        			flag_North = 1
        	if N[0] < 0:
        		flag_North = 1

        	if flag_East == 0 and E[1] < cols:
        		if board[E[0]][E[1]] == "B":
        			flag_East = 1
        		elif board[E[0]][E[1]] == "p":
        			result = result + 1
        			flag_East = 1
        	if E[1] >= cols:
        		flag_East = 1

        	if flag_South == 0 and S[0] < rows:
        		if board[S[0]][S[1]] == "B":
        			flag_South = 1
        		elif board[S[0]][S[1]] == "p":
        			result = result + 1
        			flag_South = 1
        	if S[0] >= rows:
        		flag_South = 1

        	if flag_West == 0 and W[1] >= 0:
        		if board[W[0]][W[1]] == "B":
        			flag_West = 1
        		elif board[W[0]][W[1]] == "p":
        			result = result + 1
        			flag_West = 1
        	if W[1] < 0:
        		flag_West = 1

        return result

obj = Solution()
print(obj.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))        