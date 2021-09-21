'''
72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = []

        rows = len(word1) + 1
        cols = len(word2) + 1

        for row in range(rows):
        	temp = []
        	for col in range(cols):
        		if row < rows - 1 and col == cols - 1:
        			temp.append(rows - row - 1)
        		elif row == rows - 1:
        			temp.append(cols - col - 1)
        		else:
        			temp.append(float('inf'))
        	dp.append(temp)

        for row in range(rows - 2, -1, -1):
        	for col in range(cols - 2, -1, -1):
        		if word1[row] == word2[col]:
        			dp[row][col] = dp[row + 1][col + 1]
        		else:
        			dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])

        return dp[0][0]


obj = Solution()
print(obj.minDistance(word1 = "horse", word2 = "ros"))