"""
========================
Python Data Structures
========================

List, Tuple, and Set are built-in Python data structures used to store collections of data.
"""

# ==================================================
# LIST
# ==================================================
"""
Notes:
- Lists are **ordered** and **mutable** (modifiable).
- They allow **duplicate values**.
- Indexing, slicing, and traversal work the same way as with strings.
- Lists are best suited when data needs to be updated frequently.
"""

courses = ["physics", "chemistry", "maths"]

# Length, traversal, and slicing
print(len(courses))
print(courses[:2])

# --------------------------------------------------
# Adding elements to a list (3 ways)
# --------------------------------------------------
courses_2 = ["Arts", "Commerce", ["Engineering", "MBBS"]]

courses.append("biology")        # Adds element at the end
courses.insert(0, "biology")     # Adds element at a specific index
courses.extend(courses_2)        # Adds multiple elements individually

print(courses)

# --------------------------------------------------
# Removing elements from a list
# --------------------------------------------------
courses.remove("maths")           # Removes a specific value
removed_course = courses.pop()    # Removes and returns the last element

print(courses)
print("Removed:", removed_course)

# --------------------------------------------------
# Common list methods and operations
# --------------------------------------------------
"""
1. reverse()                  -> Reverses the list in-place
2. sort()                     -> Sorts the list in ascending order
3. sort(reverse=True)         -> Sorts the list in descending order
4. min(list), max(list)       -> Returns minimum / maximum value
5. sum(list)                  -> Returns sum of numeric elements
6. list.index(value)          -> Returns index of the value (error if not found)
7. value in list              -> Returns True / False
"""

"""
sorted(list) -> Returns a new sorted list without modifying the original list
"""

# --------------------------------------------------
# Converting between strings and lists
# --------------------------------------------------
"""
1. string.split(separator)    -> Converts a string into a list
2. separator.join(list)       -> Converts a list into a string
"""

str_courses = " , ".join(courses)
print(str_courses)

new_list = str_courses.split(" , ")
print(type(new_list))


# ==================================================
# TUPLE
# ==================================================
"""
Notes:
- Tuples are **ordered** and **immutable** (cannot be modified).
- Once created, elements cannot be added, removed, or changed.
- Faster than lists and safe for fixed data.
"""

dimensions = (1920, 1080)
print(dimensions)
print(dimensions[0])


# ==================================================
# SET
# ==================================================
"""
Notes:
- Sets store **unordered** and **unique** elements.
- Duplicate values are automatically removed.
- Sets are optimized for fast membership testing.
- Sets do not support indexing or slicing.
"""

set1 = {'a', 'b', 'c'}

# Creating an empty set ({} creates a dictionary, not a set)
empty_set = set()
print(empty_set)

# Membership test (very efficient in sets)
print('a' in set1)

set2 = {'a', 'd', 'e', 'f'}

# --------------------------------------------------
# Common set operations
# --------------------------------------------------
"""
1. intersection() -> Common elements
2. difference()   -> Elements present in the first set but not in the second
3. union()        -> All unique elements from both sets
"""

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
