'''
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
        	return True
        if word[0].isupper() and word[1].isupper():
        	flag = 1
        elif word[0].islower() and word[1].islower():
        	flag = 2
        elif word[0].isupper() and word[1].islower():
        	flag = 3
        else:
        	return False
        for index in range(1, len(word)):
        	if flag == 1:
	        	if word[index].islower():
	        		return False
	        if flag == 2:
	        	if word[index].isupper():
	        		return False
	        if flag == 3:
	        	if word[index].isupper():
	        		return False

        return True

obj = Solution()
#print(obj.detectCapitalUse("USA"))
#print(obj.detectCapitalUse("Googel"))
print(obj.detectCapitalUse("GoogelG"))