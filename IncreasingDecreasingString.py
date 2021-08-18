'''
1370. Increasing Decreasing String
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
'''
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        char_freq = {}
        print s
        for char in s:
        	if char_freq.has_key(char):
        		char_freq[char] = char_freq[char] + 1
        	else:
        		char_freq[char] = 1

        chars = sorted(char_freq.keys())
        index = 0
        target = len(chars)
        direction = True
        result = []

        while size > 0:
        	if direction:
        		if char_freq[chars[index]] > 0:
        			result.append(chars[index])
        			char_freq[chars[index]] = char_freq[chars[index]] - 1
        			size = size - 1
        		index = index + 1
        	else:
        		if char_freq[chars[index]] > 0:
        			result.append(chars[index])
        			char_freq[chars[index]] = char_freq[chars[index]] - 1
        			size = size - 1
        		index = index - 1
        	if index == target:
        		direction = False
        		index = target - 1
        	if index == -1:
        		direction = True
        		index = 0

        return "".join(result)


obj = Solution()
print(obj.sortString("aaaabbbbcccc"), "abccbaabccba")
print(obj.sortString("rat"), "art") 
print(obj.sortString("leetcode"), "cdelotee") 
print(obj.sortString("ggggggg"), "ggggggg") 
print(obj.sortString("spo"), "ops") 