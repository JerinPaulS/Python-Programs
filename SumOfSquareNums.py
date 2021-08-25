'''
Sum of Square Numbers
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true
 

Constraints:

0 <= c <= 231 - 1
'''
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        val = 0
        while (val * val) <= c:
        	rem = int(math.sqrt(c - (val * val)))
        	if (rem * rem) + (val * val) == c:
        		return True
        	val = val + 1
        return False

obj = Solution()
print(obj.judgeSquareSum(3))        