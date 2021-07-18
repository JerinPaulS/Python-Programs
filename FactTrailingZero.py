'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
        	count = count + (n // 5)
        	n = n // 5
        return count

obj = Solution()
print(obj.trailingZeroes(1))
print(obj.trailingZeroes(2))
print(obj.trailingZeroes(3))
print(obj.trailingZeroes(4))
print(obj.trailingZeroes(5))
print(obj.trailingZeroes(6))
print(obj.trailingZeroes(7))