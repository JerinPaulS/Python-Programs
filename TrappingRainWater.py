'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
        	return 0
        result = 0
        start = 0
        end = len(height) - 1
        max_left = height[start]
        max_right = height[end]
        
        while start < end:
        	if max_left < max_right:        		
        		if max_left - height[start] >= 0:
        			result = result + max_left - height[start]
        		start = start + 1
        		max_left = max(max_left, height[start])
        	else:
        		if max_right - height[end] >= 0:
        			result = result + max_right - height[end]
        		end = end - 1
        		max_right = max(max_right, height[end])

        return result

obj = Solution()
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))