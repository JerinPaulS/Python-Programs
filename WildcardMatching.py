'''
44. Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "":
            return len(p) == p.count("*")            
        s1, s2 = [""] + list(s), [""] + list(p)
        
        rows, cols = len(s1), len(s2)
        dp = []
        for row in range(rows):
            temp = []
            for col in range(cols):
                temp.append("")
            dp.append(temp)
        
        dp[0][0] = True
        
        for row in range(1, rows):
            if s1[row] == "*":
                dp[row][0] = dp[row - 1][0]
        
        for col in range(1, cols):
            if s2[col] == "*":
                dp[0][col] = dp[0][col - 1]
        
        for row in range(rows):
            for col in range(cols):
                if row == col and row == 0:
                    continue
                if s1[row] == "*" or s2[col] == "*":
                    dp[row][col] = dp[row][col - 1] or dp[row - 1][col]
                elif s1[row] == "?" or s2[col] == "?":
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    if s1[row] == s2[col]:
                        dp[row][col] = dp[row - 1][col - 1]
                    else:
                        dp[row][col] = False
        return dp[-1][-1]