'''
917. Reverse Only Letters
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_s = list(s)
        start = 0
        end = len(s) - 1
        while start <= end:
        	if temp_s[start].isalpha() and temp_s[end].isalpha():
        		temp = temp_s[end]
        		temp_s[end] = temp_s[start]
        		temp_s[start] = temp
        		start = start + 1
        		end = end - 1
        	else:
	        	if temp_s[start].isalpha() == False:
	        		start = start + 1
	        	if temp_s[end].isalpha() == False:
	        		end = end - 1
        s = "".join(temp_s)
        return s


obj = Solution()
print(obj.reverseOnlyLetters("ab-cd"))        