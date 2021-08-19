'''
1417. Reformat The String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
'''
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        digits = []
        for char in s:
        	if char.isdigit():
        		digits.append(char)
        	else:
        		letters.append(char)

        print letters, digits

        letter_size = len(letters)
        digit_size = len(digits)
        if abs(letter_size - digit_size) > 1:
        	return ""
        result = ""
        ptr1 = 0
        ptr2 = 0
        flag = 0
        if digit_size > letter_size:
        	flag = 1
        index = 0
        while ptr1 < letter_size and ptr2 < digit_size:
        	if flag == 0:
        		if index % 2 == 0:
        			result = result + (letters[ptr1])
        			ptr1 = ptr1 + 1
        		else:
        			result = result + (digits[ptr2])
        			ptr2 = ptr2 + 1
        		index = index + 1
        	else:
        		if index % 2 == 0:
        			result = result + (digits[ptr2])
        			ptr2 = ptr2 + 1
        		else:
        			result = result + (letters[ptr1])
        			ptr1 = ptr1 + 1
        		index = index + 1
        while ptr1 < letter_size:
        	result = result + letters[ptr1]
        	ptr1 = ptr1 + 1       	
        while ptr2 < digit_size:
        	result = result + digits[ptr2]
        	ptr2 = ptr2 + 1
        return result

obj = Solution()
print(obj.reformat("covid2019"))        