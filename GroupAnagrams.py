'''
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = {}
        size = len(strs)
        for index in range(size):
        	s_word = "".join(sorted(strs[index]))
        	if word_dict.has_key(s_word):
        		word_dict[s_word].append(strs[index])
        	else:
        		temp = [strs[index]]
        		word_dict[s_word] = temp

        return word_dict.values()

obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))       