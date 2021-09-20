'''
583. Delete Operation for Two Strings
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
        	return 0
        dp = []
        for _ in range(len(word1) + 1):
        	dp.append([0] * (len(word2) + 1))

        for row in range(1, len(word1) + 1):
        	for col in range(1, len(word2) + 1):
        		if word1[row - 1] == word2[col - 1]:
        			dp[row][col] = dp[row - 1][col - 1] + 1
        		else:
        			dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
        return len(word1) + len(word2) - (2 * dp[-1][-1])