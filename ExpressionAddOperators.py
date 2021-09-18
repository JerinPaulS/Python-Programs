'''
Expression Add Operators
Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
'''
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def backtrack(index, prev, cur, value, s):
        	if index == size:
        		if value == target and cur == 0:
        			result.append(s)
        		return

        	cur = (cur * 10) + int(num[index])
        	if cur > 0:
        		backtrack(index + 1, prev, cur, value, s)

        	if len(s) == 0:
        		backtrack(index + 1, cur, 0, value + cur, str(cur))
        	else:
        		backtrack(index + 1, cur, 0, value + cur, s + "+" + str(cur))
        		backtrack(index + 1, -cur, 0, value - cur, s + "-" + str(cur))
        		backtrack(index + 1, prev * cur, 0, value - prev + (prev * cur), s + "*" + str(cur))

        size = len(num)
        result = []
        backtrack(0, 0, 0, 0,"")
        return result