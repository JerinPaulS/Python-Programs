'''
1252. Cells with Odd Values in a Matrix
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

 

Example 1:


Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
Example 2:


Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
 

Constraints:

1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n
 

Follow up: Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space?
'''
class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n

        for index in indices:
        	rows[index[0]] = rows[index[0]] + 1
        	cols[index[1]] = cols[index[1]] + 1

        odd_col = 0
        even_col = 0

        odd_row = 0
        even_row = 0

        for row in rows:
        	if row % 2 == 0:
        		even_row = even_row + 1
        	else:
        		odd_row = odd_row + 1

        for col in cols:
        	if col % 2 == 0:
        		even_col = even_col + 1
        	else:
        		odd_col = odd_col + 1

        return (odd_row * even_col) + (even_row * odd_col)

obj = Solution()
print(obj.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
print(obj.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))