from math import prod
from typing import Sequence

# built in functions - common operations
# ----------------------------------------------------------------------------------------------------
# getting the length of an item with built in funtion

numbers: list[int] = [1, 2, 3, 4, 5]
name: str = "Anand Sogalad"

print(f"Lenght of 'list - numbers' : {len(numbers)}")
print(f"Length of 'string - name' : {len(name)}")


# how it works internally?
def get_length(item: Sequence):
    counter = 0
    for _ in item:
        counter += 1
    return counter


# getting the same output
print(f"Lenght of 'list - numbers' : {get_length(numbers)}")
print(f"Length of 'string - name' : {get_length(name)}")

# ----------------------------------------------------------------------------------------------------

# Sorting
numbers = [-6, 7, -3, 2, 1, 9, 0]

# sorted built in funtion sorts and return new array or list
# it doesn't modify the existing array or list

sorted_list: list[int] = sorted(numbers)
print(f"Sorted list: {sorted_list}")
print(f"Original list: {numbers}")

# if we need to sort and resverse use reverse parameter
sorted_reversed_list: list[int] = sorted(numbers, reverse=True)
print(f"Sorted and reversed list: {sorted_reversed_list}")

# if I want to work on absolute value use key which take function
sorted_reversed_list: list[int] = sorted(numbers, reverse=True, key=abs)
print(f"Absolute Sorted and reversed list: {sorted_reversed_list}")

# sorting based on the lenght
names: list[str] = ["Anand", "Vijay", "Abhilash", "Niranjan"]
sorted_names: list[str] = sorted(names, key=len)
sorted_reversed_names: list[str] = sorted(names, key=len, reverse=True)

print(f"Sorted names: {sorted_names}")
print(f"Sorted and reversed names: {sorted_reversed_names}")

# if you want to modify the existing array or list use .sort() method
names.sort()
numbers.sort()

print(numbers, names)

# ----------------------------------------------------------------------------------------------------

# min, max, sum, prod, len, any, all, count, enumerate

numbers = [10, -5, -16, 11, 15, 5]
true_false: list[bool] = [True, False, True, False]

max_number, max_abs_number = max(numbers), max(numbers, key=abs)
min_number, min_abs_number = min(numbers), min(numbers, key=abs)
product_numbers = prod(numbers)
sum_numbers = sum(numbers)

print(f"max: {max_number} abs_max: {max_abs_number}")
print(f"min: {min_number} abs_min: {min_abs_number}")
print(f"product: {product_numbers}")
print(f"sum: {sum_numbers}")
print(f"len: {len(numbers)}")
print(f"any: {any(true_false)} all: {all(true_false)}")
print(f"count: {true_false.count(True)}")

print(f"enumerate: {[(i, v) for i, v in enumerate(numbers)]}")

# ----------------------------------------------------------------------------------------------------

# from collections import deque, Counter, defaultdict, OrderedDict, namedtuple
