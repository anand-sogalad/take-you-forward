import bisect
import heapq
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
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

# deque - doube ended queue

# used when fast add/remove from both ends needed
# used for implementing stack and queue
# used for sliding widnow plroblems
# used for BFS travel
dq = deque([1, 2, 3, 4, 5])  # deque([1, 2, 3, 4, 5])

dq.append(6)  # deque([1, 2, 3, 4, 5, 6])
dq.appendleft(0)  # deque([0, 1, 2, 3, 4, 5, 6])

dq.pop()  # deque([1, 2, 3, 4, 5]) and return 6
dq.popleft()  # deque([1, 2, 3, 4, 5]) and return 0

dq.extend([6, 7])  # deque([1, 2, 3, 4, 5, 6, 7])
dq.extendleft([0, -1])  # deque([-1, 0, 1, 2, 3, 4, 5, 6, 7])

dq.rotate(1)  # deque([7, -1, 0, 1, 2, 3, 4, 5, 6])
dq.rotate(2)  # deque([5, 6, 7, -1, 0, 1, 2, 3, 4])


# Counter
# Frequency counting
# Most common elements
# Anagram problems
# Frequency-based problems
counter = Counter([1, 2, 3, 4, 5, 1])

counter.get(1)  # 2
counter.most_common(2)  # [(1, 2), (2, 1)] 1, repeated 2 times and 2 1 times
print(counter.items())  # dict_items([(1, 2), (2, 1), (3, 1), (4, 1), (5, 1)])
print(list(counter.elements()))  # [1, 1, 2, 3, 4, 5]
counter.update([1, 5])  # Counter({1: 3, 5: 2, 2: 1, 3: 1, 4: 1})
counter.subtract([1])  # Counter({1: 2, 5: 2, 2: 1, 3: 1, 4: 1})


# defaultdict
# Never raises KeyError, creates default value
# Grouping elements
# Building graphs
# Avoiding KeyError checks
# Counting with auto-initialization
dd = defaultdict(int)  # Default: 0
dd["a"]  # Returns 0 (auto-created)
dd["a"] += 1  # Now dd['a'] = 1

dd_list = defaultdict(list)  # Default: []
dd_list["fruits"].append("apple")  # Auto-creates list
dd_list["fruits"]  # ['apple']

dd_set = defaultdict(set)  # Default: set()
dd_set["nums"].add(1)  # Auto-creates set
dd_set["nums"]  # {1}

dd_custom = defaultdict(lambda: "N/A")  # Custom default
dd_custom["missing"]  # Returns "N/A"


# LRU Cache implementation
# Need ordered dictionary
# Special pop operations
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od["d"] = 4  # Set value: OrderedDict([('a',1), ('b',2), ('c',3), ('d',4)])
od.move_to_end("a")  # Move to end: OrderedDict([('b',2), ('c',3), ('d',4), ('a',1)])
od.move_to_end(
    "c", last=False
)  # Move to beginning: OrderedDict([('c',3), ('b',2), ('d',4), ('a',1)])
od.popitem()  # Remove last: returns ('a', 1)
od.popitem(last=False)  # Remove first: returns ('c', 3)


# namedTuple
# Lightweight data structures
# Return multiple values
# Immutable records
# Dictionary keys
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)  # Create: Point(x=1, y=2)
p.x  # Access by name: 1
p.y  # Access by name: 2
p[0]  # Access by index: 1
p[1]  # Access by index: 2
# Immutable: p.x = 3  # ERROR! Cannot modify

# ----------------------------------------------------------------------------------------------------

# heapq
# a priority q
values = [11, 87, 54, 32, 76, 00, 99, 88, 78]
heapq.heapify(values)
heapq.heappush(values, 10)  # [10]
heapq.heappush(values, 9)  # [9, 10]

print(values)  # [9, 10] - because heap1 always sotres smallest value at first

print(heapq.heappop(values))  # always return first value that would be smallest - 9

print(heapq.heappushpop(values, 11))  # this first pushes 11 and pops smallest element
print(heapq.heapreplace(values, 0))  # this pops first and then pushes the element
print(heapq.nlargest(5, values))  # [99, 88, 87, 78, 76]
print(heapq.nsmallest(5, values))  # [0, 0, 11, 32, 54]

# we know that while pushing the elements using heapq, we get the smallest at first what if we alerady have existing list
values = [11, 87, 54, 32, 76, 00, 99, 88, 78]
heapq.heapify(values)
print(values)  # [0, 32, 11, 78, 76, 54, 99, 88, 87]

# by default it gets min value at first how to do it for max values?
heapq.heapify_max(values)
print(values)  # [99, 88, 54, 87, 76, 0, 11, 78, 32]

heapq.heappush_max(values, 100)
print(values)  # [100, 99, 54, 87, 88, 0, 11, 78, 32, 76]

# same way for every operation we have max type as well

# bisect
# can be used for binary search
values = [11, 87, 54, 32, 76, 00, 99, 88, 78]
values.sort()  # sort the array, because bisect works only on sorted list/array

bisect.bisect(
    values, 0
)  # this return right most idex in which I can insert value 0 whithout braking the sorted order

bisect.bisect_left(
    values, 0
)  # this return left most idex in which I can insert value 0 whithout braking the sorted order

bisect.insort(values, 10)  # it iserts at the right most suitable index
bisect.insort_left(values, 9)  # it iserts at the left most suitable index
