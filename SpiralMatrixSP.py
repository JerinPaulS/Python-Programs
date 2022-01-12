'''
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''
class Solution:
	def generateMatrix(self, n):
		ans = [[0]*n for i in range(n)]
		i,j = 0, 0
		dire = [0,1,0,-1,0]
		po = 0
		for a in range(1,n*n+1):
			ans[i][j] = a
			ni,nj = i+dire[po],j+dire[po+1]
			if (not 0<=ni<n) or (not 0<=nj<n) or ans[ni][nj]!=0:
				po+=1
				po%=4
				ni,nj = i+dire[po],j+dire[po+1]
			i,j = ni,nj
		return ans

obj = Solution()
print(obj.generateMatrix(10))        