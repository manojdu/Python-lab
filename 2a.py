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