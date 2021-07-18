'''
Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly
3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string 
false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks 
between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
'''
def QuestionsMarks(strParam):

  # code goes here
  a_flag = 0
  n_flag = 0
  count = 0
  res = 0
  temp = ""
  for chars in strParam:
  	if chars.isalpha():
  		a_flag = 1
  	if chars.isdigit() and n_flag == 0:
  		n_flag = 1
  		temp = temp + chars
  	elif chars.isdigit() and n_flag == 1:
  		if count != 3:
  			res = 0
  			break
  		elif int(temp) + int(chars) == 10:
  			res = 1
  			break
  	if chars == '?' and n_flag == 1:
  		count = count + 1
  if n_flag == 0 or res == 0 or a_flag == 0:
  	return("false")
  return("true")
  	
# keep this function call here 
print(QuestionsMarks(input()))