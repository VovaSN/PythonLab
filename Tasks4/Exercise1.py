def isContains(arr, elem):
  if elem in arr:
    print(f"\n{elem} is present in s")
  else:
    print(f"{elem} was not found in s")

def sequenceOperations(arr):
  """Sequence operations with python list

  	Arguments:
		arr (list)  - list for work with
  """

  print(f"\nSize of s :{len(arr)}")

  assert len(s) > 0 

  isContains(arr, 2)
  isContains(arr, 4)

  print(f"\nFirst element is: {arr[0]}")
  print(f"Last element is: {arr[-1]}")

  print(f"\n1 frequency is: {arr.count(1)}")

  arr.pop(2)
  print("\nRemove element at index 2 of s")

  arr.remove(2)
  print("\nRemove element 2 from s")

  arr.append(7)
  print("\nAdd 7 at the end of s")

  arr.insert(2,6)
  print("\nAdd 6 in position 2 in s")

  insertBeforeX(arr, 1, 0)
  print(f"\nAdd 0 before the first occurrence of x = 1 in s")

  print(f"\nSum of squares: {sumOfSquares(arr)}")

  print(s)

def insertBeforeX(arr, x, insertValue):
  if x in arr:
    index = arr.index(x)
    arr.insert(index, insertValue)

def sumOfSquares(arr):
  return sum(x**2 for x in arr) 
 
s =[9,1,5,2,1,3]

print(s)

sequenceOperations(s)