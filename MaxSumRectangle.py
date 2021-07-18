'''
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

 

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105
 
 [[2,2,-1]]
 0

[[ 5,-4,-3, 4],
 [-3,-4, 4, 5],
 [ 5, 1, 5,-4]],10

Follow up: What if the number of rows is much larger than the number of columns?
'''
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        curr_max = -106
        result = []
        sum_arr = 0
        temp_arr = [0] * len(matrix)
        for left_col in range(len(matrix[0])):
        	temp_arr = [0] * len(matrix)
        	for right_col in range(left_col, len(matrix[0])):
        		for row in range(len(matrix)):
        			temp_arr[row] = temp_arr[row] + matrix[row][right_col]
        		curr_max = temp_arr[0]
        		sum_arr = temp_arr[0]
        		for row in range(len(matrix)):
        			if row > 0:
    					curr_max = curr_max + temp_arr[row]
    					sum_arr = sum_arr + temp_arr[row]
    				if curr_max not in result:
    					result.append(curr_max)
    				if sum_arr not in result:
    					result.append(sum_arr)
    				if temp_arr[row] > curr_max:
    					curr_max = temp_arr[row]

    	result = sorted(result)
    	start = 0
    	end = len(result) - 1
    	print(result, start, end)
    	while(start <= end):
    		mid = int((start + end) / 2)
    		if result[mid] < k:
    			start = mid + 1
    		elif result[mid] > k:
    			end = mid - 1
    		else:
    			return(result[mid])
        return(result[start - 1])

obj = Solution()
#print(obj.maxSumSubmatrix([[1,0,1],[0,-2,3]], k = 2))
#print(obj.maxSumSubmatrix([[2,2,-1]], k = 3))
#print(obj.maxSumSubmatrix([[2,2,-1]], k = 0))
#print(obj.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], k = 10))
#print(obj.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], k = 8))
print(obj.maxSumSubmatrix([[5,-4,-3,4],[-3,-4,4,5],[5,1,5,-4]], k = -1))
#print(obj.maxSumSubmatrix([[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]],12))

'''
def maxSumSubmatrix(self, matrix, k):
        result = -sys.maxint
        m, n = len(matrix), len(matrix[0])
        hSum = [[0 for j in range(n+1)] for i in range(m)]
        for i in range(m):
            for j in range(1, n+1):
                hSum[i][j] = hSum[i][j-1] + matrix[i][j-1]
        for ColA in range(1, n+1):
            for ColB in range(ColA, n+1):
                slist, vSum = [0], 0
                for row in range(m):
                    vSum += hSum[row][ColB] - hSum[row][ColA-1
]                    ind = self.search(slist, vSum-k)
                    if ind < len(slist):
                        result = max(result, vSum - slist[ind])
                    index = self.search(slist, vSum)
                    slist.insert(index, vSum)
        return result
    def search(self, slist, val): 
        left, right = 0, len(slist) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if slist[mid] >= val:
                right = mid - 1
            else:
                left = mid + 1
        return left   

'''