'''
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?

'''
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def index_finder(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row) - start
        
        count = 0
        for row in grid:
            count = count + index_finder(row)
        return count

obj = Solution()
#print(obj.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
#print(obj.countNegatives([[3,2],[1,0]]))
#print(obj.countNegatives([[1,-1],[-1,-1]]))
print(obj.countNegatives([[8,-2,-2,-2,-4,-5,-5],[-2,-3,-3,-4,-4,-5,-5],[-2,-5,-5,-5,-5,-5,-5],[-3,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5]]))  