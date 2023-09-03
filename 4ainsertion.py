arr = [38, 30, 8, 29, 49, 46, 7, 25, 37, 13, 42]
print("Unsorted list", arr)
for i in range(1, len(arr)):
  key = arr[i]
  j = i-1
  while j >= 0 and key < arr[j]:
    arr[j+1] = arr[j]
    j = j - 1
    arr[j+1]=key
print("Sorted list", arr)
