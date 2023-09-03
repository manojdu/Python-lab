#4b)Write a program to convert roman numbers in to integer values using dictionaries

def roman_to_int(roman):
  roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'c':100, 'D':500, 'M':1000}
  sum = 0
  flag = 0
  if roman in roman_dict.keys():
    for i in range(len(roman)):
      val = roman_dict[roman[i]]
      if i + 1 < len(roman) and roman_dict[roman[i+1]] > val:
        sum = sum - val
      else:
        sum = sum + val
    return sum
  else:
    print("Invalid Input")
    exit()
roman = input("Enter a roman numeral: ")
num = roman_to_int(roman)
print("Integer value: ",num)
