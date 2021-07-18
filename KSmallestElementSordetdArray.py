'''
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        mat_max = matrix[len(matrix) - 1][len(matrix) - 1]
        mat_min = matrix[0][0]
        while mat_min < mat_max:
        	mid = (mat_max + mat_min) // 2
        	if self.count_ele(mid, matrix) < k:
        		mat_min = mid + 1
        	else:
        		mat_max = mid

        return mat_max

    def count_ele(self, ele, matrix):
    	count = 0
    	row = 0
    	col = len(matrix) - 1
    	while row < len(matrix) and col >= 0:
    		if matrix[row][col] <= ele:
    			count = count + col + 1
    			row = row + 1
    		else:
    			col = col - 1
    	return count

obj = Solution()
print(obj.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], k = 8))
print(obj.kthSmallest([[-5]], k = 1))