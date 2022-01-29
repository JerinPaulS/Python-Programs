'''
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        size = len(heights)

        for index, height in enumerate(heights):
        	if len(stack) == 0:
        		stack.append((index, height))
        	elif len(stack) > 0:
        		top = stack[-1][1]
        		if height > top:
        			stack.append((index, height))
        		else:
        			temp = index
        			while len(stack) > 0 and stack[-1][1] > height:
        				i, h = stack.pop()
        				max_area = max(max_area, (index - i) * h)
        				temp = i
        			stack.append((temp, height))
        	print(stack, max_area)

        while len(stack) > 0:
        	i, h = stack.pop()
        	max_area = max(max_area, (size - i) * h)

        return max_area

obj = Solution()
print(obj.largestRectangleArea([0, 0]))        