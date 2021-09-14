'''
Reverse Only Letters
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
        s = list(s)
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:
        	if s[ptr1].isalpha() and s[ptr2].isalpha():
        		s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
        		ptr1 = ptr1 + 1
        		ptr2 = ptr2 - 1
        	elif not s[ptr1].isalpha():
        		ptr1 = ptr1 + 1
        	elif not s[ptr2].isalpha():
        		ptr2 = ptr2 - 1
        return "".join(s)