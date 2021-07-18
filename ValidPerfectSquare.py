'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num
        while start <= end:
        	mid = (start + end) // 2
        	if (mid * mid) < num:
        		start = mid + 1
        	else:
        		end = mid - 1
        if start * start == num:
        	return True
        else:
        	return False

obj = Solution()
print(obj.isPerfectSquare(2))
print(obj.isPerfectSquare(3))
print(obj.isPerfectSquare(4))
print(obj.isPerfectSquare(5))
print(obj.isPerfectSquare(16))
print(obj.isPerfectSquare(121))