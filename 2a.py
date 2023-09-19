#2a) Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a value for N (where N >0) as input and pass this value to the function. Display suitable error message if the condition for input value is not followed.

def fibnoacci(n):
  if n <= 0:
    return "Error: Invalid input"
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    fib_list = [0, 1]
    for i in range(2,n):
      fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list[-1]

n = int(input("Enter the value of N: "))
result = fibnoacci(n)
print("Fibonacci sequence value at position {} : {} ".format(n,result))