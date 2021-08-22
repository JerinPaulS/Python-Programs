'''
Rectangle Area II
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.
 

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 109
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
'''
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        MOD = (10 ** 9) + 7
        INF_MIN = - 2 ** 32
        events = []

        for rect in rectangles:
        	x1, y1, x2, y2 = rect
        	events.append([x1, 0, y1, y2])
        	events.append([x2, 1, y1, y2])

        events.sort(key = lambda x: (x[0], x[1]))

        def calc_area(mult):
        	area = 0
        	prev = INF_MIN
        	for left, right in open_interval:
        		prev = max(prev, left)
        		area = area + max(0, (right - prev) * mult)
        		prev = max(right, prev)
        	return area

        area = 0
        prev = INF_MIN
        open_interval = []
        for event in events:
        	curr, close, y1, y2 = event
        	area = area + calc_area(curr - prev)
        	if close:
        		open_interval.remove((y1, y2))
        	else:
        		open_interval.append((y1, y2))
        		open_interval.sort()
        	prev = curr

        return area % MOD

obj = Solution()
print(obj.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))        