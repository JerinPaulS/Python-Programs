'''
1044. Longest Duplicate Substring
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

 

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.
'''
class Hasher:
    
    def __init__(self, string, base=26, modulo=2**32):
        self.base = base
        self.modulo = modulo
        self.string = string
        self.char_codes = [self.charcode(ch) for ch in string]
    
    def hash(self, left, right):
        '''hashes the string between indices [left, right)'''
        hash_code = 0
        for ch_idx in range(left, right):
            hash_code = (hash_code * self.base + self.char_codes[ch_idx]) % self.modulo
        return hash_code
    
    def hash_roll(self, hash_code, size, left, right):
        '''copmutes the new hash_code by appending the rightmost and removing the leftmost character'''
        left_coef = self.left_coefficient(size)
        hash_code = (hash_code * self.base - self.char_codes[left] * left_coef + self.char_codes[right]) % self.modulo
        return hash_code
    
    @functools.lru_cache(None)
    def left_coefficient(self, size):
        return self.base ** size % self.modulo
    
    @functools.lru_cache(None)
    def charcode(self, ch):
        return ord(ch) - ord('a')
    

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        hasher = Hasher(string=S)
        
        def find_duplicate(size):
            '''searches for a duplicate of a given size and returns if found'''
            hashpos = {}  # position of a hash
            
            rolling_hash = hasher.hash(0, size)
            hashpos[rolling_hash] = 0
            for i in range(1, len(S)-size+1):
                rolling_hash = hasher.hash_roll(rolling_hash, size, i-1, i+size-1)
                if rolling_hash in hashpos:
                    sub_start = hashpos[rolling_hash]
                    sub_end = sub_start + size
                    if S[sub_start:sub_end] == S[i:i+size]:  # hash collision
                        return S[sub_start:sub_end]
                hashpos[rolling_hash] = i
            return ''
        
        left, right = 1, len(S)
        maxdup = ''
        while left < right:
            mid = (left + right) // 2
            dup = find_duplicate(mid)
            if len(dup) > len(maxdup):
                maxdup = dup
                left = mid + 1
            else:
                right = mid
        
        return maxdup