'''
Find Intersection
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
Examples
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
'''
def FindIntersection(strArr):

  # code goes here
  i = 0
  temp_i = 0
  j = 0
  temp_j = 0
  list1 = []
  list2 = []
  while i < len(strArr[0]):
  	if strArr[0][i] == ',':
  		list1.append(int(strArr[0][temp_i:i]))
  		temp_i = i + 1
  	elif i == len(strArr[0]) - 1:
  		list1.append(int(strArr[0][temp_i:len(strArr[0])]))
  		temp_i = i + 1
  	elif strArr[0][i] == ' ':
  		temp_i = temp_i + 1
  	i = i + 1
  while j < len(strArr[1]):
  	if strArr[1][j] == ',':
  		list2.append(int(strArr[1][temp_j:j]))
  		temp_j = j + 1
  	elif  j == len(strArr[1]) - 1:
  		list2.append(int(strArr[1][temp_j:len(strArr[1])]))
  		temp_j = j + 1
  	elif strArr[1][j] == ' ':
  		temp_j = temp_j + 1
  	j = j + 1
  i = 0
  j = 0
  result = ""
  while i < len(list1) and j < len(list2):
  	if list1[i] == list2[j]:
  		result = result + str(list1[i]) + ","
  		i = i + 1
  		j = j + 1
  	else:
  		if list1[i] > list2[j]:
  			j = j + 1
  		else:
  			i = i + 1
  	if i + 1 < len(list1):
  		if list1[i] == list1[i + 1]:
  			i = i + 1
  	if j + 1 < len(list2):
  		if list2[j] == list2[j + 1]:
  			j = j + 1

  if result == "":
  	return("false")
  else:
  	return result[:-1]

# keep this function call here 
print(FindIntersection(input()))