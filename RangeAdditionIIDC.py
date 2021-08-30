'''
Range Addition II
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9
 

Constraints:

1 <= m, n <= 4 * 104
1 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
'''
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n

        for op in ops:
        	for row in range(op[0]):
        		rows[row] = rows[row] + 1
        	for col in range(op[1]):
        		cols[col] = cols[col] + 1

        row_index = 0
        col_index = 0

        while row_index < m and rows[row_index] == rows[0]:
        	row_index = row_index + 1
        while col_index < n and cols[col_index] == cols[0]:
        	col_index = col_index + 1

        return col_index * row_index