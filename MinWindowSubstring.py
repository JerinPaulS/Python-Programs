'''
Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
import collections
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		temp = dict(Counter(t))
	    count = len(temp)

	    i, j = 0, 0
	    start = ""
	    mini = 10 ** 6

	    while j < len(s):

	        if s[j] in temp:
	            temp[s[j]] -= 1
	            if temp[s[j]] == 0:
	                count -= 1

	        while count == 0 and i <= j:

	            if (j - i + 1) < mini:
	                mini = (j - i + 1)
	                start = s[i: j + 1]

	            if s[i] in temp:
	                temp[s[i]] += 1
	                if temp[s[i]] == 1:
	                    count += 1

	            i += 1
	        j += 1
	        
	    return start
		
obj = Solution()
print(obj.minWindow(s = "a", t = "a"))

'''
		if s == "" or t == "" or len(t) > len(s):
			return ""
		char_freq = collections.Counter(t)
		size = len(s)
		left = 0
		right = size - 1
		count = len(t)
		minLength = size + 1
		found = False

		i = 0
		j = 0

		while j < size:
			if count > 0:
				if char_freq.has_key(s[j]):
					char_freq[s[j]] = char_freq[s[j]] - 1
					if char_freq[s[j]] == 0:
						count = count - 1
				j = j + 1

			if count == 0:
				if char_freq.has_key(s[i]):
					char_freq[s[i]] = char_freq[s[i]] + 1
					if char_freq[s[i]] > 0:
						count = count + 1
					if j - i < minLength:
						left = i
						right = j
						minLength = j - i
						found = True
				i = i + 1
		while i < size and char_freq.has_key(s[i]) == False:
			i = i + 1
		if j - i < minLength:
			left = i
			right = j
			minLength = j - i
		if found:
			if left == right:
				return s[left - 1: right]
			return s[left:right]
		else:
			return ""

''' 