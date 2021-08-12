'''
1037. Valid Boomerang
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
 

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
'''
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # y = mx + c
        # m = (y2 - y1) / (x2 - x1)
        # c = x1.y2 - x2.y1
        (x0, y0), (x1, y1), (x2, y2) = points
        return (y2 - y1) * (x0 - x1) != (x2 - x1) * (y0 - y1)

obj = Solution()
print(obj.isBoomerang([[0,0],[0,2],[2,1]]))        	