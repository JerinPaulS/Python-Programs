'''
Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cache = {}

        def dfs(i, j):
        	if j == len(t):
        		return 1
        	if i == len(s):
        		return 0
        	if cache.has_key((i, j)):
        		return cache[(i, j)]

        	if s[i] == t[j]:
        		cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        	else:
        		cache[(i, j)] = dfs(i + 1, j)
        	return cache[(i, j)]

        return dfs(0, 0)