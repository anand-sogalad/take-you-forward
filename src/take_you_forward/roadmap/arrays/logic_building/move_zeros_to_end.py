"""
Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.
"""
def move_zeros_to_end(arr: list[int])-> list[int]:
  left = 0
  for i in range(len(arr)):
    if arr[i] != 0:
      arr[left], arr[i] = arr[i], arr[left]
      left += 1
  return arr 

if __name__ == "__main__":
  result = move_zeros_to_end([1, 2, 3, 0, 1, 0, 0, 4, 5])
  print(result)
