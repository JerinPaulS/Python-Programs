'''
1556. Thousand Separator
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31
'''
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
        	return "0"
        result = ""
        count = 0
        while n > 0:
        	if count == 3:
        		count = 0
        		result = str(n % 10) + "." + result
        	else:
        		result = str(n % 10) + result
        	n = n // 10
        	count = count + 1
        return result