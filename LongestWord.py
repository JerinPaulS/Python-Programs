'''
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
'''
def LongestWord(sen):

  # code goes here
  sen = sen.split()
  max_len = 0
  max_wrd = ""
  for word in sen:
  	flag = 0
	if len(word) > max_len and word.isalnum() == True:
		max_len = len(word)
		max_wrd = word
  return max_wrd

# keep this function call here 
print(LongestWord(input()))