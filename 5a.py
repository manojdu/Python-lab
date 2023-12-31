#5a) Write a function called isphonenumber () to recognize a pattern 415-555-4242 without using regular expression and also write the code to recognize the same pattern using regular expression.

def isphonenumber(number):
  if len(number) != 12:
    return False
  for i in range(0,3):
    if not number[i].isdigit():
      return False
  if number[3] != '-':
    return False
  for i in range(4, 7):
    if not number[i].isdigit():
      return False
  if number[7] != '-':
    return False
  for i in range(8, 12):
    if not number[i].isdigit():
      return False
  return True
phone_number = input("Enter a phone number: ")
if isphonenumber(phone_number):
  print("Valid phone number")
else:
  print("Invalid phone number")