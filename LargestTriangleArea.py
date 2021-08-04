'''
812. Largest Triangle Area
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
'''
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        size = len(points)

        def calcArea(a, b, c):
        	return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[0] * c[1] + c[0] * b[1] + b[0] * a[1])) / 2

        for i in range(size - 2):
        	for j in range(i + 1, size - 1):
        		for k in range(j + 1, size):
        			temp_area = calcArea(points[i], points[j], points[k])
        			max_area = max(temp_area, max_area)

        return max_area

obj = Solution()
print(obj.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0],[-3,3],[3,-3]]))