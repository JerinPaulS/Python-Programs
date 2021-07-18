'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        curr_res = [1]
        result.append(curr_res)
        if numRows == 1:
        	return result
        
        count = 1
        for i in range(1, numRows):
        	count = count + 1
        	curr_res = []
        	if count > numRows:
        		break
        	for j in range(count):
        		if j == 0 or j == (count - 1):
        			curr_res.append(1)
        		else:
        			curr_res.append(result[i - 1][j - 1] + result[i - 1][j])
        	result.append(curr_res)

        return result

obj = Solution()
print(obj.generate(1))
print(obj.generate(2))
print(obj.generate(3))
print(obj.generate(4))
print(obj.generate(5))