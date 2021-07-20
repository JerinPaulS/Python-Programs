'''
504. Base 7
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
        	return "0"
        result = ""
        if num < 0:
        	result = "-"
        	num = num * -1
        remainder = 0
        count = 0
        while num > 0:
        	remainder = ((num % 7) * (10 ** count)) + remainder
        	num = num // 7
        	count = count + 1
        result = result + str(remainder)
        return result

obj = Solution()
print(obj.convertToBase7(100))