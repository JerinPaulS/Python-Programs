'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

 

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:

Input: n = "82734"
Output: 8

Example 3:

Input: n = "27346209830709182346"
Output: 9

Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
'''
'''
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        N = []
        for i in range(len(n)):
        	N.append(int(n[i]))
        count = 0
        for i in range(len(N)):
        	if N[i] != 0:
        		count = count + N[i]
	        	for j in range(i + 1, len(N)):	        		
	        			if N[i] >= N[j]:
	        				N[j] = 0
	        			else:
	        				N[j] = N[j] - N[i]
	        	N[i] = 0
        	
        print(count)
'''
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        print(max(s))

obj = Solution()
obj.minPartitions("32")
obj.minPartitions("82734")
obj.minPartitions("27346209830709182346")