'''
1784. Check if Binary String Has at Most One Segment of Ones
Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
s[0] is '1'.
'''
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ones_count = 0
        for char in s:
        	if char == "1":
        		ones_count = ones_count + 1
        flag = 0
        for index in range(len(s)):        	
        	if flag == 0 and s[index] == "1":
        		flag = 1
        	if flag == 1:
        		if s[index] == "1":
        			ones_count = ones_count - 1
	        	elif s[index] != "1" and ones_count != 0:
	        		return False
        return ones_count == 0