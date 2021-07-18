'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_count = collections.Counter(s)
        res_length = 0
        flag = 0
        for val in freq_count.keys():        	
            res_length = res_length + freq_count[val]
            if freq_count[val] % 2 != 0:
                res_length = res_length - 1
                flag = 1
        if flag == 1:
            res_length = res_length + 1
        return res_length