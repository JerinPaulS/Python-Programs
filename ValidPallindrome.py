'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_inp = ""
        for index in range(len(s)):
        	if s[index].isalnum():
        		str_inp = str_inp + s[index].lower()
        if len(str_inp) == 0:
            return True
       	start = 0
       	end = len(str_inp) - 1
       	while start <= end:
       		if str_inp[start] != str_inp[end]:
       			return False
       		start = start + 1
       		end = end - 1
       		print "Hello"
        return True

obj = Solution()
#print(obj.isPalindrome("A man, a plan, a canal: Panama"))
#print(obj.isPalindrome("race a car"))
print(obj.isPalindrome("0P"))