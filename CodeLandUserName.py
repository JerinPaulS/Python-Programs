'''
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true

'''
def test(strTemp):
  for i in range(len(strTemp)):
    if strTemp[i].isalnum() == False:
      if strTemp[i] != '_':
        return("False")
  return("True")


def CodelandUsernameValidation(strParam):

  # code goes here
  if len(strParam) < 4 or len(strParam) > 25:
    return("false")
  if strParam[0].isalpha() == False:
    return("flase")
  if strParam[-1] == '_':
    return("flase")
  if test(strParam) == "False":
    return("false")
  
  return("true")

# keep this function call here
print(CodelandUsernameValidation(input()))

'''
  if len(string) < 4 or len(string) > 24:
    return "false"
  if string[-1] == "_":
    return "false"
  if not string[0].isalpha():
    return "false"
  for elem in string:
    if not elem.isalpha() and not elem.isdigit() and not elem == "_":
      return "false"
  return "true"
'''