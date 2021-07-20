'''
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 

'''
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        result = []
        for word in words:
        	temp = set(word)
        	if temp == temp.intersection(row1) or temp == temp.intersection(row2) or temp == temp.intersection(row3):
        		result.append(word)
        return result

obj = Solution()
print(obj.findWords(["Hello","Alaska","Dad","Peace"]))
print(obj.findWords(["omk"]))
print(obj.findWords(["adsdf","sfd"]))