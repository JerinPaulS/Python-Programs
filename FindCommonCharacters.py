'''
1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''
import collections
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        target = collections.Counter(words[0])
        subset = words[1:]
        list_keys = target.keys()
        for alpha in list_keys:
        	count = target[alpha]
        	for word in subset:
        		temp = word.count(alpha)
    			count = min(count, temp)
    		result = result + [alpha] * count

    	return result

obj = Solution()
#print(obj.commonChars(["bella","label","roller"]))
print(obj.commonChars(["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"]))