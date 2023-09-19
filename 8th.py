#Write a python program to find the whether the given input is palindrome or not (for both string and integer) using the concept of polymorphism and inheritance.
class PalindromeChecker:
  def if_palindrome(self, input):
    pass

class StringPalindromeChecker(PalindromeChecker):
  def if_palindrome(self, input):
    return input == input[::-1]

class IntegerPalindromeChecker(PalindromeChecker):
  def if_palindrome(self, input):
    return input == input[::-1]

string_checker = StringPalindromeChecker()
integer_checker = IntegerPalindromeChecker()

Stringinput = input("Enter the String input: ")

if string_checker.if_palindrome(Stringinput):
  print("The String is Palindrome.")
else:
  print("The String is not Palindrome.")

Intinput = input("Enter the Integer input: ")

if integer_checker.if_palindrome(Intinput):
  print("The Integer is Palindrome.")
else:
  print("The Integer is not Palindrome.")