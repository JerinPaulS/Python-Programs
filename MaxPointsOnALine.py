'''
149. Max Points on a Line
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''
import sys
import collections
from decimal import *
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def get_slope(p1, p2):
        	y_diff = p2[1] - p1[1]
        	x_diff = p2[0] - p1[0]

        	if x_diff == 0:
        		return sys.maxsize
        	return Decimal(y_diff) / Decimal(x_diff)

        result = 0

        for i in range(len(points)):
        	temp = []
        	same = 0
        	for j in range(len(points)):
        		if i != j:
        			if points[i] == points[j]:
        				same = same + 1
        			else:
        				temp.append(get_slope(points[i], points[j]))
        	count = collections.Counter(temp)
            res = 0
        	if count.values():
        		res = max(count.values())
        	result = max(result, res + same + 1)

        return result