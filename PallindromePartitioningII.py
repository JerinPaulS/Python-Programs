'''
Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        pallin = []
        dp = []
        size = len(s)

        inf = 20000

        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(False)
            pallin.append(temp)
            dp.append(0)

        iterate = 0

        while iterate < size:
            i = 0
            j = iterate

            while j < size:
                if iterate == 0:
                    pallin[i][j] = True
                elif iterate == 1:
                    if s[i] == s[j]:
                        pallin[i][j] = True
                    else:
                        pallin[i][j] = False
                else:
                    if s[i] == s[j] and pallin[i + 1][j - 1] == True:
                        pallin[i][j] = True
                    else:
                        pallin[i][j] = False

                i = i + 1
                j = j + 1
            iterate = iterate + 1

        for index in range(1, size):
            if pallin[0][index] == True:
                dp[index] = 0
            else:
                min_count = inf

                for i in range(index, 0, -1):
                    if pallin[i][index] == True:
                        if dp[i - 1] < min_count:
                            min_count = dp[i - 1]

                dp[index] = min_count + 1

        return dp[size - 1]

obj = Solution()
print(obj.minCut("abccbc"))

'''
	a	a	b
---------------
a | 0   0	1
a | x	0	1
b | x	x	0

'''