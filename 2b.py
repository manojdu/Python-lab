#2b) Develop a python program to convert binary to decimal, octal to hexadecimal using functions.

def binary_to_decimal(binary):
  return(int(binary,2))

def octal_to_decimal(octal):
  return(int(octal,8))

binary = input("Enter a binary number: ")
decimal = binary_to_decimal(binary)
print("Binary {} in decimal: {}".format(binary,decimal))

octal = input("Enter a octal number: ")
decimal = octal_to_decimal(octal)