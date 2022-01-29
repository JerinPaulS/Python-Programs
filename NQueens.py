'''
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
'''
class Solution:
    def solveNQueens(self, n):
        result = []
        board = []
        for _ in range(n):
            board.append(["."] * n)

        cols = set()
        posDiag = set()
        negDiag = set()

        def backTrack(row):
            if row == n:
                temp = []
                for row in board:
                    temp.append("".join(row))
                result.append(temp)
                return
            for col in range(n):
                if col in cols or (row - col) in negDiag or (row + col) in posDiag:
                    continue

                cols.add(col)
                negDiag.add(row - col)
                posDiag.add(row + col)
                board[row][col] = "Q"

                backTrack(row + 1)

                cols.remove(col)
                negDiag.remove(row - col)
                posDiag.remove(row + col)
                board[row][col] = "."

        backTrack(0)
        return result

obj = Solution()
print(obj.solveNQueens(4))        