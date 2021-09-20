'''
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1)
        len2 = len(text2)
        dp = []
        for row in range(len1 + 1):
        	temp = []
        	for col in range(len2 + 1):
    			temp.append(0)
        	dp.append(temp)

        for row in range(len1 - 1, -1, -1):
        	for col in range(len2 - 1, -1, -1):
        		if text1[row] == text2[col]:
        			dp[row][col] = dp[row + 1][col + 1] + 1
        		else:
        			dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]