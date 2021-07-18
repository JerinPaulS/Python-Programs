'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        curr_res = [1]
        result.append(curr_res)
        if rowIndex == 0:
        	return result[rowIndex]
        count = 1
        col = rowIndex + 1
        for i in range(1, col + 1):
        	count = count + 1
       		curr_res = []
       		if count == rowIndex + 2:
       			break
       		for j in range(count):
       			if j == 0 or j == (count - 1):
       				curr_res.append(1)
       			else:
       				curr_res.append(result[i - 1][j - 1] + result[i - 1][j])
       		result.append(curr_res)
       	return result[rowIndex]

obj = Solution()
print(obj.getRow(0))
print(obj.getRow(1))
print(obj.getRow(2))
print(obj.getRow(3))
print(obj.getRow(4))