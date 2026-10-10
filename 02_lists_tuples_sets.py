"""Topic 2: lists, indexing, slicing, tuples, sets."""

names = ["Manoj", "Ann", "Raj"]
salaries = [50000, 29000, 35000]

# Indexing: starts at 0. Negative counts from the end.
#  index:     0       1      2
#  negative: -3      -2     -1
print(names[0])      # Manoj
print(names[2])      # Raj
print(names[-1])     # Raj (same item as names[2])
print(salaries[1])   # 29000 (same index, different list, different value)

# Slicing: start included, end EXCLUDED
print(names[0:2])      # ['Manoj', 'Ann']
print(names[1:3])      # ['Ann', 'Raj']
print(names[:1])       # ['Manoj'] (still a list)
print(names[-2:])      # ['Ann', 'Raj']
print(names[-3:-1])    # ['Manoj', 'Ann']

# Lists are mutable (changeable)
names[1] = "Lee"
print(names)           # ['Manoj', 'Lee', 'Raj']

# List comprehension
print([s for s in salaries if s > 30000])   # [50000, 35000]

# Tuple: like a list but fixed. Unpacking is the useful part.
emp = ("Ann", 29000, "Chennai")
print(emp[1])          # 29000
name, sal, city = emp  # unpacking


def min_max(nums):
    return min(nums), max(nums)   # returns a tuple


lo, hi = min_max([7, 3, 10, 1])
print(lo, hi)          # 1 10

# Set: no duplicates, unordered (like SELECT DISTINCT)
print(len({5, 5, 6, 7, 7}))        # 3
print(len(set([1, 1, 1, 2])))      # 2

# {} is an empty DICT. Use set() for an empty set.
print(type({}), type(set()))
