def get_range(arr, target):
  first, last = -1, -1  
  for i, n in enumerate(arr):
    if n == target:
      if first == -1:
	first = i
	last = i
      else:
	last = i

  return [first, last]
    
def binary_search(arr, target):
  lower, upper = 0, len(arr) - 1
  while lower <= upper:
    mid_point = (upper + lower)/2
    if arr[mid_point] < target:
      lower = mid_point + 1
    elif arr[mid_point] > target:
      upper = mid_point - 1
    elif arr[mid_point] == target:
      return mid_point
  return None

arr = [1,2,34,87,87,87,90]
print(binary_search(arr, 87))
print(binary_search(arr, 7))
  
