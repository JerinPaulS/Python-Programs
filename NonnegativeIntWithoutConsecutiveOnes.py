'''
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

 

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3
 

Constraints:

1 <= n <= 109
'''
class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        fibb = [0] * 32
		fibb[0] = 1
		fibb[1] = 2

		for i in range(2, 32):
			fibb[i] = fibb[i - 1] + fibb[i - 2]

		i = 30
		res_count = 0
		prev = 0

		while i >= 0:
			if (n & (1 << i)) != 0:
				res_count = res_count + fibb[i]
				if prev == 1:
					res_count = res_count - 1
					break
				prev = 1
			else:
				prev = 0

			i = i - 1 

		return res_count + 1